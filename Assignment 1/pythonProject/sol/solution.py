# This function computes all possible following states (neighbors) from the current state of a puzzle by shifting the
# empty tile (represented by 8) left, right, up, or down. It recognizes the position of the empty tile,
# calculates valid moves within the puzzle's boundaries, and creates new states by swapping the empty tile with
# adjacent tiles. This aids in investigating all possible configurations for solving the issue, which is necessary for
# search algorithms such as A* or iterative deepening.

# Function to Find Neighbours of Current State
# The neighbours() function returns a list of possible neighbours
def neighbours(node):
    # Finding where the empty tile (8) is
    empty_index = node.index(8)

    # Calculating its row and column
    row = int(empty_index / 3)
    col = int(empty_index % 3)

    # Moves for left, right, up, down
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # List to store neighbors of the current state
    valid_neighbors = []

    # Looping through possible moves
    for move in moves:

        # New row and column after the move
        new_row = row + move[0]
        new_col = col + move[1]

        # Check if the move is within bounds
        if (0 <= new_row and new_row < 3) and (0 <= new_col and new_col < 3):
            # New index based on new row and column
            new_index = new_row * 3 + new_col

            # Copy the current state
            new_node = node[:]
            # Swap the empty tile with the new position
            new_node[empty_index], new_node[new_index] = new_node[new_index], new_node[empty_index]
            # Add the new state to neighbors list
            valid_neighbors.append(new_node)

    # Return the neighbors of the current state
    return valid_neighbors



# The iterativeDeepening function specifies a depth-first search (DFS) approach for solving the challenge.
# The DFS searches all potential paths up to a specified depth for a series of movements that turns the beginning state into the goal state.
# It uses a path list to track the sequence of moves and ensures that no states from the same branch are revisited.
# If it discovers the desired state within the depth limit, it returns the swap sequence from the empty tile (8). Otherwise,
# it will retreat and try alternative courses until it reaches the depth limit.
def iterativeDeepening(puzzle):
    # Depth First Search
    def dfs(current_state, depth, path, goal_state):
        # If depth is 0 and current state is the goal, return the swap sequence
        if depth == 0 and current_state == goal_state:
            # List to store the swap sequence
            swap_list = []
            # For each state leading to the goal
            for i in path[1:]:
                # Find the index of 8 (blank space) in the path
                swap_list.append(i.index(8))
            # Return the list of swap sequences
            return swap_list
        elif depth > 0:
            # Loop through each neighbor of the current state
            for neighbour in neighbours(current_state):
                # Visit the neighbor only if it hasn't been visited in this branch
                if tuple(neighbour) not in visited:
                    # Mark this neighbor as visited
                    visited.add(tuple(neighbour))
                    # Recursively call DFS with decreased depth
                    result = dfs(neighbour, depth - 1, path + [neighbour], goal_state)
                    # If DFS finds the goal state
                    if result:
                        # Return the result
                        return result
                    # Remove the neighbor from visited set if this path fails
                    visited.remove(tuple(neighbour))
            # Return empty if no solution found at this depth
            return []

# This snippet defines the iterative deepening search strategy for solving the challenge.
# It iterates through various depth limitations, using the depth-first search (DFS) approach with increasing depths.
# The goal is to extensively search the solution space while keeping memory use under control.
# If a valid solution is found within the depth limit, the result is returned; otherwise,
# the search is repeated until the maximum depth is achieved. This guarantees that the search is systematic and
# progresses to deeper layers, providing for a balance of completeness and quickness in discovering the solution.
    # Defining Goal State
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # Loop through different depth limits
    for depth_limit in range(1, 50):  # Increased range to cover larger depths
        # Set to track visited states
        visited = set()
        # Call DFS for the current depth limit
        result = dfs(puzzle, depth_limit, [puzzle], goal_state)
        # If DFS returns a valid result
        if result:
            # Return the result to the main function
            return result
    # Return an empty list if no solution is found
    return []

    # Defining Goal State
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # Loop through different depth limits
    for depth_limit in range(1, 50):  # Increased range to cover larger depths
        # Set to track visited states
        visited = set()
        # Call DFS for the current depth limit
        result = dfs(puzzle, depth_limit, [puzzle], goal_state)
        # If DFS returns a valid result
        if result:
            # Return the result to the main function
            return result
    # Return an empty list if no solution is found
    return []

# This function uses the A* search method to determine the best solution to the puzzle.
# It makes use of the Manhattan distance heuristic to calculate the cost of getting from one state to another.
# The function iterates through the states, computing their total cost (f value) and prioritizing exploration according
# to the lowest heuristic cost. It keeps an open set of unknown states and a closed collection of explored ones to avoid
# revisiting them. If the goal state is discovered, it returns the sequence of moves (swap indexes) required to get there;
# otherwise, it produces an empty list if no solution is found.
def astar(puzzle):
    # Defining the goal state
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Function to calculate the heuristic value using Manhattan distance
    def heuristic(node):
        # Total distance starts at zero
        total_distance = 0
        # Calculate the Manhattan distance for each tile
        for i in range(0, 9):
            # Index of the tile in the current node
            a = node.index(i)
            # Index of the tile in the goal node
            b = goal_state.index(i)
            # Add the distance to the total
            total_distance += abs(int(a / 3) - int(b / 3)) + abs(a % 3 - b % 3)
        # Return the total heuristic cost
        return total_distance

    # Function to calculate the total cost (f value)
    def f(node, g):
        return heuristic(node) + g

    # List to keep track of (heuristic cost, state, path to this state)
    open_set = [(heuristic(puzzle), puzzle, [puzzle])]
    # Set to track visited states
    closed_set = set()

    # Iterate through states in the open set
    while open_set:
        # Sort states to get the one with the lowest heuristic cost
        open_set.sort()
        # Get the state with the minimum heuristic cost
        current_tuple = open_set.pop(0)
        # Unpack the tuple into separate variables
        heuristic_cost, current_node, path = current_tuple

        # If the current state is the goal state
        if current_node == goal_state:
            # List to store the indexes where 8 was swapped
            swap_index = []
            # Iterate through the path starting from the second state
            for i in path[1:]:
                # Append the index of 8 in each state to swap_index
                swap_index.append(i.index(8))
            # Return the swap indexes
            return swap_index

        # Otherwise, if the current node is not the goal state, add it to the explored set
        closed_set.add(tuple(current_node))

        # Iterate through each neighbor of the current state
        for neighbour in neighbours(current_node):
            # If the neighbor has not been explored yet
            if tuple(neighbour) not in closed_set:
                # Calculate the cost to reach this neighbor
                g_value = len(path)
                # Calculate the total cost (f value) for the neighbor
                f_value = f(neighbour, g_value)
                # Add the neighbor to the open set
                open_set.append((f_value, neighbour, path + [neighbour]))

    # If no solution is found, return an empty list
    return []

# Example run of Iterative Deepening
a = iterativeDeepening([0, 4, 1, 3, 8, 2, 6, 7, 5])
print("Iterative Deepening Output:", a)

# Example run of A* Algorithm
a = astar([0, 4, 1, 3, 8, 2, 6, 7, 5])
print("A* Algorithm Output:", a)


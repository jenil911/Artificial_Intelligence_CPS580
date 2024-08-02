import random

def initialize_state_values(episodes):
    """
    Initialize state values randomly between 0 and 5.

    :param episodes: List of episodes where each episode is a list of (state, action, reward, new_state)
    :return: Dictionary with state as key and its initialized value
    """
    state_values = {}
    # Go through each episode
    for episode in episodes:
        # Go through each step in the episode
        for step in episode:
            # Convert the state to a tuple
            state = tuple(step[0])
            # If the state is not already in state_values, add it with a random value
            if state not in state_values:
                state_values[state] = random.uniform(0, 5)  # Randomly initialize between 0 and 5
    return state_values

def compute_temporal_difference(episodes, gamma=0.9, alpha=0.1, num_iterations=1000):
    """
    Compute the Temporal Difference value for each state.

    :param episodes: List of episodes where each episode is a list of (state, action, reward, new_state)
    :param gamma: Discount factor for future rewards
    :param alpha: Learning rate
    :param num_iterations: Number of iterations for updating state values
    :return: Dictionary with state as key and its computed value as value
    """
    # Initialize state values randomly
    state_values = initialize_state_values(episodes)

    # Update state values through multiple iterations
    for _ in range(num_iterations):
        # Go through each episode
        for episode in episodes:
            # Go through each step in the episode
            for step in episode:
                state = tuple(step[0])  # Current state
                action = step[1]       # Action taken
                reward = step[2]       # Reward received
                new_state = tuple(step[3])  # Next state

                # Compute the Temporal Difference target
                if new_state in state_values:
                    td_target = reward + gamma * state_values[new_state]
                else:
                    td_target = reward

                # Compute the Temporal Difference error
                td_error = td_target - state_values[state]
                # Update the state value using the learning rate
                state_values[state] += alpha * td_error

    return state_values

# Example usage from custom data to test
if __name__ == "__main__":
    # Example episodes (main.py would typically load these from a file)
    episodes = [
        [([0, 0], 'right', 1, [0, 1]), ([0, 1], 'down', 2, [1, 1])],
        [([1, 1], 'left', -1, [0, 1]), ([0, 1], 'up', 0, [0, 0])]
    ]

    # Compute state values using Temporal Difference learning
    state_values = compute_temporal_difference(episodes)
    print("Computed State Values:", state_values)

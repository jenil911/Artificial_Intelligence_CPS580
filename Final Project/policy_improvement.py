def improve_policy(state_values, episodes, gamma=0.9):
    """
    Improve the policy based on state values.

    :param state_values: Dictionary where each key is a state and each value is the computed value for that state
    :param episodes: List of episodes where each episode is a list of (state, action, reward, new_state)
    :param gamma: Discount factor for future rewards
    :return: Improved policy where each key is a state and the value is the best action to take from that state
    """
    # Define the possible actions
    actions = ['up', 'down', 'left', 'right']

    # Initialize an empty dictionary to store the improved policy
    policy = {}

    # Iterate over all states in state_values to determine the best action for each state
    for state in state_values:
        best_action = None
        max_value = -float('inf')  # Start with a very low value to find the maximum

        # Evaluate all possible actions for the current state
        for action in actions:
            total_value = 0
            count = 0

            # Calculate the expected value of taking this action from the current state
            for episode in episodes:
                for step in episode:
                    # Check if the current step matches the state and action being evaluated
                    if tuple(step[0]) == state and step[1] == action:
                        next_state = tuple(step[3])
                        reward = step[2]
                        # If the next state is known, use its value; otherwise, use 0
                        if next_state in state_values:
                            total_value += reward + gamma * state_values[next_state]
                        else:
                            total_value += reward
                        count += 1

            # Average value for this action
            if count > 0:
                average_value = total_value / count
            else:
                # Use a default value if no data is available for this action
                average_value = state_values.get(state, 0)

            # Debug: Print action values for analysis
            print(
                f"State: {state}, Action: {action}, Total Value: {total_value}, Count: {count}, Average Value: {average_value}")

            # Update the best action if this action has a higher value
            if average_value > max_value:
                max_value = average_value
                best_action = action

        # Assign the best action for the current state to the policy
        policy[state] = best_action

        # Debug: Print the best action and its value for the state
        print(f"State: {state}, Best Action: {best_action}, Max Value: {max_value}")

    print("")  # Print a blank line for spacing
    return policy


# Example usage, we select certain states, and assign State values to them and see what policy would be test
if __name__ == "__main__":
    # Example states and actions
    states = [(0, 0), (0, 1), (1, 0), (1, 1)]
    actions = ['up', 'down', 'left', 'right']

    # Example state values (these would typically come from TD learning)
    state_values = {
        (0, 0): 1.5,
        (0, 1): 2.0,
        (1, 0): 1.0,
        (1, 1): 3.0
    }

    # Example episodes
    episodes = [
        [([0, 0], 'right', 1, [0, 1]), ([0, 1], 'down', 2, [1, 1])],
        [([1, 1], 'left', -1, [0, 1]), ([0, 1], 'up', 0, [0, 0])]
    ]

    # Improve the policy based on state values and episodes
    policy = improve_policy(state_values, episodes)
    print("Updated Policy:", policy)

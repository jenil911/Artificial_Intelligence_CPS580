# Import functions from other modules
from data_loader import load_episodes
from temporal_difference import compute_temporal_difference
from policy_improvement import improve_policy


def main():
    # Specify the path to the JSON file with training data
    file_path = 'C:/Udayton/AI/Final Project/sOjK115D.json'

    # Load the episodes data from the specified file
    episodes = load_episodes(file_path)
    print("")  # Print a blank line for spacing

    # Compute state values based on the episodes using Temporal Difference (TD) learning
    state_values = compute_temporal_difference(episodes)
    print("Computed State Values:", state_values)  # Display the computed state values
    print("")  # Print a blank line for spacing

    # Improve the policy using the computed state values and episodes
    policy = improve_policy(state_values, episodes)
    print("")  # Print a blank line for spacing

    # Display the improved policy
    print("Computed Policy:", policy)


# execute the main function
if __name__ == "__main__":
    main()

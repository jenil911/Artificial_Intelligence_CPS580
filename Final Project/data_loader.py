import json


def load_episodes(file_path):
    """
    Load episodes from a JSON file.

    Parameters:
    - file_path (str): The path to the JSON file containing the episodes.

    Returns:
    - episodes (list): A list of episodes, where each episode is a list of
      state-action-reward-new_state tuples.
    """

    # Open the JSON file and read its contents
    with open(file_path, 'r') as file:
        data = json.load(file)

    episodes = []

    # Go through each episode in the JSON data
    for episode in data:
        episode_list = []

        # Go through each step in the episode
        for step in episode:
            # Get the state from the step and turn it into a tuple
            state = tuple(step[0])

            # Get the action from the step
            action = step[1]

            # Get the reward from the step
            reward = step[2]

            # Get the new state from the step and turn it into a tuple
            new_state = tuple(step[3])

            # Add the state, action, reward, and new state as a tuple to the episode list
            episode_list.append((state, action, reward, new_state))

        # Add the full episode list to the episodes list
        episodes.append(episode_list)

    # Return the list of episodes
    return episodes


# Loading My Personal Data into The Console
file_path = "C:/Udayton/AI/Final Project/sOjK115D.json"
episodes = load_episodes(file_path)
print(episodes)

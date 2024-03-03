import requests


def fetch_user_repositories(username):
    """Function to fetch user repositories from GitHub API"""

    # Construct the GitHub API URL for user repositories
    url = f"https://api.github.com/users/{username}/repos"

    # Make a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a list of repositories
        repos = response.json()
        return repos
    else:
        # Print an error message if the request was not successful
        print(f"Status code: {response.status_code}")
        return None


def display_repository_info(repositories):
    """Function to display information about user repositories"""

    # Check if there are repositories to display
    if repositories is not None:
        # Iterate through each repository and print relevant information
        for repo in repositories:
            print(f"Repository Name: {repo['name']}")
            print(f"Description: {repo['description'] or 'No description'}")
            print(f"Language: {repo['language'] or 'Not specified'}")
            print(f"Stars: {repo['stargazers_count']}")
            print("=================================")
    else:
        # Print a message if there are no repositories to display
        print("No repositories to display.")


def main():
    """Main function to execute the program"""

    # Prompt the user to enter a GitHub username
    username_input = input("Enter a username: ")

    # Fetch user repositories using the provided username
    fetch = fetch_user_repositories(username_input)

    # Check if the fetch was successful
    if fetch is None:
        print(f"Failed to fetch repositories")
    else:
        # Display information about the fetched repositories
        display_repository_info(fetch)


# Execute the main function
main()


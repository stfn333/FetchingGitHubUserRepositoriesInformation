# GitHub Repository Information Fetcher

This Python script allows you to fetch and display information about a GitHub user's repositories, including details such as repository name, description, programming language, and the number of stars.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Script Overview](#script-overview)
  - [fetch_user_repositories(username)](#fetch_user_repositoriesusername)
  - [display_repository_info(repositories)](#display_repository_inforepositories)
  - [main()](#main)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python installed on your machine
- Required Python libraries: `requests`

## Usage

1. Clone the repository or download the script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script 
5. Enter the GitHub username when prompted.
6. View information about the user's repositories.

## Script Overview

### fetch_user_repositories(username)
This function fetches information about a GitHub user's repositories using the GitHub API.

Input: GitHub username
Output: List of repositories or None if the request fails

### display_repository_info(repositories)
This function displays information about the fetched repositories.

Input: List of repositories
Output: Prints repository information

### main()
The main function executes the entire script.

Prompts the user to enter a GitHub username.
Fetches user repositories using the provided username.
Displays information about the fetched repositories.

## Contributing
Contributions are welcome! Feel free to open issues or pull requests.

## License
This project is licensed under the MIT License.

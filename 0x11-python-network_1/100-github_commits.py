#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""


import requests
import sys


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner_name,
                                                              repository_name)

    response = requests.get(url)

    commits = response.json()
    for index, commit in enumerate(commits):
        if index > 10:
            break
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")

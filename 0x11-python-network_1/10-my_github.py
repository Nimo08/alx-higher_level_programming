#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    auth = (username, password)
    try:
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data["id"]
            print(user_id)
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print("None")

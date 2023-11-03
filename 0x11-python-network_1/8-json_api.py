#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    data = {"q": letter}
    response = requests.post(url, data)
    if response.headers.get("content-type") == "application/json":
        response_json = response.json()
        if response_json:
            print("[{}] {}".format(response_json.get("id"),
                                   response_json.get("name")))
        else:
            print("No result")
    else:
        print("Not a valid JSON")

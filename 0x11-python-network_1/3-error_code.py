#!/usr/bin/python3
"""
Takes in a URL and an email, sends a request to
the URL and displays the body of the response
(decoded in utf-8)
"""


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read().decode('utf-8')
            print(page)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

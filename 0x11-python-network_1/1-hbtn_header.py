#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
found in the header of the response
"""


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    variable = 'X-Request-Id'
    with urllib.request.urlopen(url) as response:
        if variable in response.headers:
            value = response.headers[variable]
            print(f"{value}")

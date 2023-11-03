#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
found in the header of the response
"""


import requests
import sys


url = sys.argv[1]
variable = 'X-Request-Id'
req = requests.get(url)
if variable in req.headers:
    value = req.headers[variable]
    print(f"{value}")

#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests
"""


import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type('utf8 string')}")
    print(f"\t- content: {req.text}")

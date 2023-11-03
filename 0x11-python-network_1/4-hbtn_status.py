#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests
"""


import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"    - type: {type('utf8 string')}")
    print(f"    - content: {req.text}")

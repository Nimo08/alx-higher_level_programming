#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests
"""


import requests


req = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print(f"    - type: {type(req.text)}")
print(f"    - content: {req.text}")

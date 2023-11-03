#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    body_string = body.decode('utf-8')
    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {body_string}")

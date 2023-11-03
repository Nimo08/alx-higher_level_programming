#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


import urllib.request
import sys


url = sys.argv[1]
email = sys.argv[2]
val = {'url': url, 'email': email}
data = urllib.parse.urlencode(val)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    page = response.read()
    page_string = page.decode('utf-8')
    print(page_string)

#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -s -i "$1" | grep -i "Allow" | cut -d ':' -f 2 | grep -E 'OPTIONS|HEAD|PUT'

#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -s -X OPTIONS -I "$1" | grep -i "Allow" | cut -d' ' -f2-

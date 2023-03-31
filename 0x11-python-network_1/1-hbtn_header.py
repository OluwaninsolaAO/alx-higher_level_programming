#!/usr/bin/python3
""" sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as r:
    print(r.getheader('X-Request-Id'))

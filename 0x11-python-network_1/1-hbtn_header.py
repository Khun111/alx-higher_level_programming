#!/usr/bin/python3
import urllib.request
import sys
url = sys.argv[1]
with urllib.request.urlopen(url) as res:
    response = res.getheader('X-Request-Id')
print(response)

#!/usr/bin/python3
'''Value of custom header with requests'''
import requests
import sys
url = sys.argv[1]
res = requests.get(url)
print(res.headers.get('X-Request-Id'))

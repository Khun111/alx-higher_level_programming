#!/usr/bin/python3
import urllib.request
import sys
'''Sends request and displays value of custom header'''
if __name__ == '__main__':
    url = sys.argv[1]
    flex_req = urllib.request.Request(url)
    with urllib.request.urlopen(flex_req) as res:
        response = res.getheader('X-Request-Id')
        print(response)

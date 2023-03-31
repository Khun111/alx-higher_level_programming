#!/usr/bin/python3
'''Sends request and displays value of custom header'''
import urllib.request
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        response = res.getheader('X-Request-Id')
        print(response)

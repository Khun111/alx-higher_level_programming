#!/usr/bin/python3
'''Sends POST request with email data'''
import urllib.request
import urllib.parse
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    user_mail = sys.argv[2]
    e_data = urllib.parse.urlencode({'email': user_mail}).encode('ascii')
    with urllib.request.urlopen(url, e_data) as res:
        response = res.read().decode('utf-8')
        print(response)

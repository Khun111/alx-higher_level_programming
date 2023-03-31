#!/usr/bin/python3
import urllib.request
import sys
'''Sends POST request with email data'''
if __name__ == '__main__':
    url = sys.argv[1]
    user_mail = sys.argv[2]
    e_data = urllib.parse.urlencode({'email': user_mail}).encode('utf-8')
    with urllib.request.urlopen(url, e_data) as res:
        response = res.read().decode('utf-8')
        print(response)

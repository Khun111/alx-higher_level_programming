#!/usr/bin/python3
'''Display github id using auth'''
import requests
import sys
if __name__ == '__main__':
    name = sys.argv[1]
    pat = sys.argv[2]
    url = 'https://api.github.com/user'
    res = requests.post(url, auth=(name, pat))
    print(res.json().get('id')) if res else print('None')
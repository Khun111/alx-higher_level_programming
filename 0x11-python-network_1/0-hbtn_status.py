#!/usr/bin/python3
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as res:
    response = res.read()
print('Body response:')
print(f'\t- type: {type(response)}')
print(f'\t- content: {response}')
print(f'\t- utf8 content: {response.decode("utf-8")}')

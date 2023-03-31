#!/usr/bin/python3
'''Fetch with requests'''
import requests
url = 'https://alx-intranet.hbtn.io/status'
res = requests.get(url)
re
print('Body response:')
print(f'\t- type: {type(response.text)}')
print(f'\t- content: {response.text}')

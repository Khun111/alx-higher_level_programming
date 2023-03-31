#!/usr/bin/python3
'''Fetch with requests'''
import requests
url = 'https://alx-intranet.hbtn.io/status'
res = requests.get(url)
print('Body response:')
print(f'\t- type: {type(res.text)}')
print(f'\t- content: {res.text}')

#!/usr/bin/python3
'''Fetch with requests'''
import requests
url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url).json()
print('Body response:')
print(f'\t- type: {type(response)}')
print(f'\t- content: {response}')

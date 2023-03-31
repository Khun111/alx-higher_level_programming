#!/usr/bin/python3
'''Handle error codes with requests'''
import requests
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    try:
        res = requests.get(url)
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as e
        print(f'Error code: {e.response.status_code}')

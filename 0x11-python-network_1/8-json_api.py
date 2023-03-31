#!/usr/bin/python3
'''Handle error codes with requests'''
import requests
import sys
if __name__ == '__main__':
    alpha = sys.argv[1] if len(sys.argv) == 2 else ''
    url = 'http://0.0.0.0:5000/search_user'
    q_data = {'q': alpha}
    res = requests.post(url, data=q_data)
    try:
        res = res.json()
        print(f'[{res.get("id")}], i\
{res.get("name")}') if res else print('No result')
    except ValueError:
        print('Not a valid JSON')

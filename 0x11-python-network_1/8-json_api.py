#!/usr/bin/python3
'''Testing json format of response'''
import requests
import sys
if __name__ == '__main__':
    alpha = '' if len(sys.argv) == 1 else sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    q_data = {'q': alpha}
    res = requests.post(url, data=q_data)
    try:
        res = res.json()
        print(f'[{res.get("id")}] \
{res.get("name")}') if res else print('No result')
    except ValueError:
        print('Not a valid JSON')

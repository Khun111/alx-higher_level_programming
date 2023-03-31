#!/usr/bin/python3
'''Display github id using auth'''
import requests
import sys
if __name__ == '__main__':
    user = sys.argv[1]
    repo = sys.argv[2]
    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    res = requests.get(url)
    res = res.json()
    for details in res[:10]:
        sha = res.get('sha')
        author = res.get('commit').get('author').get('name')
        print(sha + ': ' + author)

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
    for details in res[:10][::-1]:
        sha = details['sha']
        author = details['commit']['author']['name']
        print(sha + ': ' + author)

#!/usr/bin/python3
"""a Python script that takes 2 arguments in order to solve
this challenge"""

if __name__ == '__main__':
    import sys
    import requests
    import json

    repo, owner = sys.argv[1:]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    headers = {'Accept': 'application/vnd.github+json'}
    r = requests.get(url, headers=headers)
    try:
        res = json.loads(r.text)
        for i in range(10):
            sha = res[i]['sha']
            name = res[i]['commit']['author']['name']
            print('{}: {}'.format(sha, name))

    except IndexError:
        pass

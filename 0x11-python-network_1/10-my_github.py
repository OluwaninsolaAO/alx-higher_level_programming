#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

if __name__ == '__main__':
    import sys
    import requests
    import json

    username, passwd = sys.argv[1:]
    url = 'https://api.github.com/users/' + username
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': 'Bearer ' + passwd}
    r = requests.get(url, headers=headers)
    user = json.loads(r.text)
    try:
        print(user['id'])
    except KeyError:
        print('None')

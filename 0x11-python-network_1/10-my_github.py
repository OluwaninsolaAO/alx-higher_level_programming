#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

if __name__ = '__main__':
    import sys
    import requests
    
    username, passwd = sys.argv[1:]
    url = 'https://api.github.com/user'
    headers = {'Accept

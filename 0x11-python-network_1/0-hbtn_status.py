#!/usr/bin/python3
""" A Python script that fetches from
https://alx-intranet.hbtn.io/status """
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as r:
    res = r.read()
    print('Body response:')
    print('\t- type: {}'.format(type(res)))
    print('\t- content: {}'.format(res))
    print('\t- utf8 content: {}'.format(res.decode('utf-8')))

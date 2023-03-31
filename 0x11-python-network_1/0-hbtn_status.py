#!/usr/bin/python3
""" A Python script that fetches from
https://alx-intranet.hbtn.io/status """
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as r:
    print('Body response:')
    print('\t- type: {}'.format(type(r.read())))
    print('\t- content: {}'.format(r.read()))
    print('\t- utf8 content: {}'.format(r.read().decode('utf-8')))

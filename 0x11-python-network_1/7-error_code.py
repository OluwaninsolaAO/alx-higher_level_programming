#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)

    if r.status_code == 200:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))

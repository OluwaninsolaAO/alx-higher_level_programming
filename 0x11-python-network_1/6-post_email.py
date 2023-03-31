#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response"""

if __name__ == "__main__":
    import requests
    import sys

    url, email = sys.argv[1:]
    data = {'email': email}

    r = requests.post(url, data=data)
    print(r.text)

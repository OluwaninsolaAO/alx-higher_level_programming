#!/bin/bash
# displays only the status code of http status code
curl -s -w '%{http_code}' "$1" -o /dev/null

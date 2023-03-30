#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -w '%{http_code}' -o /dev/null -s $1 | grep 200 -q && curl -s $1 || true

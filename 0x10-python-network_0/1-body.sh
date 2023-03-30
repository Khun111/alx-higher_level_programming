#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
RES=$(curl -w '%{http_code}' -o /dev/null -s $1)
if [ $RES == 200 ]; then
  curl -s $1
fi

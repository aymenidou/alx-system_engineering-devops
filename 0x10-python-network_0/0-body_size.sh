#!/bin/bash
# store the url in a variable
url=$1

# Use curl to send a request and capture the response body size in bytes
response_size=$(curl -sI "$url" | grep -i content-length | awk '{print $2}' | tr -d '\r\n')
echo "${response_size}"

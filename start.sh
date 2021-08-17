#!/bin/bash

# create a variable to use as docker tag
application="syncall"

# build image with the tag
docker build -t ${application} .

# run the in detached mode and map port 5000 on both host and container
docker run -d -p 5000:5000 \
--name=${application} \
-v "$PWD" ${application}
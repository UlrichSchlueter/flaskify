#!/bin/bash

docker tag flask-rest-test localhost:5000/flask-rest-test:latest
docker push localhost:5000/flask-rest-test 

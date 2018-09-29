#!/bin/bash

IMAGES=$(docker images | grep -Po '(?<=remme\/)[a-z-]+(?=\s+latest)')

for IMAGE in $IMAGES; do
    docker rmi remme/$IMAGE:latest
done

if [ -d "./docs/html" ]; then
    rm -rf ./docs/html
fi

#!/bin/bash

# clean final remme images
IMAGES=$(docker images | grep -Po 'remme\/[a-z-]+(?=\s+latest)')
for IMAGE in $IMAGES; do
    docker rmi $IMAGE:latest
done

# clean intermediate remme images
IMAGES=$(docker images | grep -Po 'remme-local-[a-z-]+(?=\s+latest)')
for IMAGE in $IMAGES; do
    docker rmi $IMAGE:latest
done

if [ -d "./docs/html" ]; then
    rm -rf ./docs/html
fi

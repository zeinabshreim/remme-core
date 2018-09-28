#!/bin/sh

ADDITIONAL_ARGS=""

git submodule update --init
docker-compose -f ./build/docker-compose.yml build
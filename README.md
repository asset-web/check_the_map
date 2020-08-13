# Check the Map Python/Django/Wagtail.io (redevelopment - in progress)

[![Requirements Status](https://requires.io/github/asset-web/check_the_map/requirements.svg?branch=master)](https://requires.io/github/asset-web/check_the_map/requirements/?branch=master)

[![Build Status](https://travis-ci.org/asset-web/check_the_map.svg?branch=master)](https://travis-ci.org/asset-web/check_the_map)

# Basic build test image

    docker build . -t check_the_map:latest
    docker run --publish 8000:8000 --detach --name ctm check_the_map:latest

# Clean up

    docker stop ctm && docker rm ctm
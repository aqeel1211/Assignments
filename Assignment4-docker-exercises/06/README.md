# Description

## Run instructions

Run the following commands

    docker run -it --name=test1 alpine:latest date
    docker run -it --name=test1 alpine:latest date

Why does this not work?

What can you do to make them both run (there are at least a couple of ways)?

## Solution

    change the name of both containers
    docker run -it --name test1 alpine:latest
    docker run -it --name test2 alpine:latest

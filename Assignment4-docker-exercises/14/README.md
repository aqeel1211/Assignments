# Description
Use inspect to get metadata for a resource.

## Run instructions

    docker network create testthing
    docker volume create testthing
    docker run --name=testthing alpine date
    docker image tag alpine testthing

Now try this

    docker inspect testthing

## Solution
Did you get the output that you expected?

    If we run docker inspect testthing,it will inpsect the container
Which resource did you get the output for?

    Got output from every resource named testthing
How can you get the metadata for exactly what you want?

    Being specific about the type of resource

For volume metadeta:

    docker volume inspect testthing
For image metadeta:

    docker image inspect testthing
For network metadeta:

    docker network inspect testthing


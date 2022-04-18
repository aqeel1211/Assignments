# Description
in the docker-compose file add a delay before a service starts

## Run instructions

//Add the following attribute to the service which needs to be delayed
healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost:3000"]
    interval: 30s
    timeout: 10s
    retries: 5
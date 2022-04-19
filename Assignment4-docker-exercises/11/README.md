# Description
What command will most quickly tell you what is contained in an Alpine Linux /etc/hosts file?

## Solution
    docker run alpine cat /etc/hosts
If the container is running in background

    docker exec -it bash | cat /etc/hosts

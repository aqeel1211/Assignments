# Description

If you have a already running container that you need to pass a file to how can you send that file to it?

## Solutions

Copy file from host to container:

    docker cp foo.txt container_id:/foo.txt

Copy file from container to host:

    docker cp container_id:/foo.txt foo.txt

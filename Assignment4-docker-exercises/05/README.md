# Description
What size image does this Dockerfile create?
What size of archive does it create if you export it to a tarball?
What else is in the image that was built?

## Solution
What size image does this Dockerfile create?

    docker build -t imagetask05 .
    docker images |grep imagetask05| awk '{print $7}'
    2B

What size of archive does it create if you export it to a tarball?

    docker save -o imagestask05.tar imagetask05
    ls -lh imagestask05.tar | awk '{print $5}'
    11K
    
What else is in the image that was built?

    tar xvf imagestask05.tar
    a new folder and a json file that informs about the docker version,architetcure and env variables etc. the image was created with

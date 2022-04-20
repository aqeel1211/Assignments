# Description
Write a couple of shell scripts that will ping pong back and forth with each other and run them as containers.

## Solution

Run container1 with following command
 
    docker run -it --name container1 alpine
    
Extract its ip-address with the following command

    ifcongfig | grep inet | grep -v 127.0.0.1 | awk '{print $2}' | cut -d: -f2
    

Run container2 with the following command

    docker run -it --name container2 alpine
    
Create a script named **ping.sh** in container2 as follows

    #!bin/sh
    if ping -c 1 <container1-ip>

    then
        echo "pong"

    else
        echo "container 1 not serving requests"
    fi
    
Run the script on container2 with the following command

    sh ping.sh
  




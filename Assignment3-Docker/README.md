# Assignment3-Docker
## Basic Docker Excercises
### Daemonizing Your First Container
- Running a container in detached mode

Go to [Daemonizing your first container](https://github.com/aqeeleurus/Assignments/tree/master/Assignment3-Docker/Basic-docker-excercises/daemonizing-your-first-container) to view more on it

### Understanding Basic Commands
- Ran basic commands on docker container (docker ps, docker ps -a, docker inspect, docker logs etc)

Go to [understanding basic commands](https://github.com/aqeeleurus/Assignments/tree/master/Assignment3-Docker/Basic-docker-excercises/understanding-basic-commands) to view more on it

### Environment Variables
- Created a mongo-db container from docker-compose and included its image, ports, environment variables (username and password) in the docker-compose

Go to [environment varibles task](https://github.com/aqeeleurus/Assignments/tree/master/Assignment3-Docker/Basic-docker-excercises/Environment-variables) to view more on it

### Volumes and Ports Settings
- Using the docker run command, started an nginx container and mapped it to different host port
- Used the volume tag to persist data

Go to [volumes and ports settings](https://github.com/aqeeleurus/Assignments/tree/master/Assignment3-Docker/Basic-docker-excercises/volumes-and-ports-settings) to view more on it

---
## Intermediate Docker Excercises
### Docker Registry
- Created a repo on dockerHub
- Logged into docker from terminal
- Pushed the existing image onto the repo alongwith the tag

Go to [docker registry](https://github.com/aqeeleurus/Assignments/tree/master/Assignment3-Docker/Intermediate-docker-excercises/docker-registry) to view more on it

### Sharing Docker Daemon
- Created a dockerfile from alpine base image
- Opened docker-cli in the alpine using RUN command
- Built the dockerfile and named the image to alpine-docker
- Ran the dockerfile with -v and shared the host's docker socket  with alpine-docker

Go to [sharing docker daemon](https://github.com/aqeeleurus/Assignments/tree/master/Assignment3-Docker/Intermediate-docker-excercises/sharing-docker-daemon) to view more on it

### Writing Your First Dockerfile
- Created a dockerfile from alpine base image
- Installed pip, python and awscli
- Set the entrypoint to usr/bin/aws and ran configure command
Go to [writing yout first dockerfile](https://github.com/aqeeleurus/Assignments/tree/master/Assignment3-Docker/Intermediate-docker-excercises/writing-your-first-dockerfile) to view more on it

### Writing Your First Docker-Compose
- Created a dockerfile from python base image
- installed all the requirements
- Created config for nginx to use it as proxy server
- Created a docker-compose file to run flask,redis and nginx proxy server
- Created main.py to count reload hits on a page and stored the hits in redis
- Dockerized the app
Go to [writing yout first dockercompose](https://github.com/aqeeleurus/Assignments/tree/master/Assignment3-Docker/Intermediate-docker-excercises/writing-your-first-docker-compose-file) to view more on it
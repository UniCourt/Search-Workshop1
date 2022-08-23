## Docker post-installation setup
Optional configuration for Linux to work better with Docker.

### Run Docker as a non-root user
To create the docker group and add your user:

1. Create the docker group.
```
sudo groupadd docker
```
2. Add your user to the docker group.
```
sudo usermod -aG docker $USER
```

3. Activate the changes to groups:
```
newgrp docker 
```
4. Verify that you can run docker commands without sudo.
```
docker images
```

<br />

## Docker Commands
Docker is a containerization system that packages and runs the application with its dependencies inside a container. 
There are several docker commands you must know when working with Docker.
### 1. Docker version
To find the installed docker version
Command:
```
docker  --version
``` 
Example:
```
docker --version
Docker version 19.03.9, build 9d988398e7
```

<br>

### 2. Downloading image
To work with any Docker image we need to download the docker image first.<br /> 
Command:
```
docker pull <IMAGE>
```
Example of pulling alpine:latest image
```
docker pull alpine:latest
```

<br>

### 3. List all the docker images
To list all the images that are available in the host machine.
<br />
Command:
```
docker images
```
Example:

```
REPOSITORY  TAG     IMAGE ID        CREATED      SIZE
alpine      latest  c059bfaa849c    6 weeks ago  5.59MB
```

### 3. Run docker image
The `docker run` command is used to launch Docker containers.

When an operator executes `docker run`, the container process that runs is isolated in that it has its own file system, networking, and its own isolated process tree separate from the host.
<br>
Command:
```
docker run [options] <IMAGE>
```
> Explore options [here](https://docs.docker.com/engine/reference/run/)


Example of running alpine:latest image, the options -t allows us to access the terminal and -i gets stdin stream added. Basically using -ti adds the terminal driver.
```
docker run -t -i alpine:latest
or
docker run -ti alpine:latest

exit
```

<br>

### 4. Running containers
Let us check what containers are running currently, The command. `docker ps` will list only running containers
<br>
Command:
```
docker ps
```
Example:
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
8973c7347905        alpine:latest       "/bin/sh"           2 minutes ago       Up 2 minutes                            ecstatic_jang
```
<br />

### 5. Access the docker container
The `docker exec` command runs a new command in a running container. We’ll need to provide docker exec with the 
name (or container ID) of the container we want to work with. We can find this information using the `docker ps` command:
<br />
Command to execute into container:
```
docker exec [OPTIONS] <CONTAINER_ID> COMMAND
```
> Explore options [here](https://docs.docker.com/engine/reference/commandline/exec/)

Example: Execute into running `alpine:latest` container. Let us create one directory and a simple blank text file 
inside the container.
```
docker exec -ti 8973c7347905 sh
/ # mkdir demo
/ # cd demo
/demo # touch helloworld.txt
/demo # ls
helloworld.txt
/demo # 
```
`mkdir` command to create a directory or folder<br />
`cd` change directory used to change the current working directory <br />
`touch` command to create a blank file<br />
<br />

### 6. Stop the container
Now let us stop the running container 
<br />
Command:
```
docker stop [OPTIONS] <CONTAINER_ID>
```
> Explore options [here](https://docs.docker.com/engine/reference/commandline/stop/)

Example of stopping alpine:latest running container
```
docker stop 8973c7347905
```
Here once you stop the container, the container is still available locally, but it is not in the running state.<br  />

### 7. List all the containers
`docker ps -a` will list all the containers including stopped containers.
<br/>
Example output:
```
mis@mispl-lap-19:~$ docker ps -a
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS                       PORTS                                                 NAMES
4cc4008815d8        alpine:latest             "/bin/sh"                57 minutes ago      Exited (137) 2 minutes ago
```

<br />

### 8. Start the container
Let's start the stopped `alpine:latest` container again.
<br />
Command:
```
docker start [OPTIONS] <CONTAINER_ID>
```
> Explore options [here](https://docs.docker.com/engine/reference/commandline/start/)


Example of starting alpine:latest container. Before starting the container we need the container id, 
so let's get the container id by `docker ps -a` command.
```
docker ps -a

docker start 4cc4008815d8
```

### 9. Remove the container 
You can remove the container or multiple containers by `docker rm` command.<br />
Command
```
docker rm [OPTIONS] <CONTAINER...>
```
> Explore Options [here](https://docs.docker.com/engine/reference/commandline/rm/)
Example:
```
docker rm 4cc4008815d8
```
Note: Execute this only after you stop the container
<br />

### 10. Removing image
You can remove the local images by `docker rmi` command.
<br />
Command:
```
docker rmi [OPTIONS] <IMAGE_ID> / <IMAGE_ID...>
```
Example: Remove alpine:latest image
```
docker rmi c059bfaa849c
```
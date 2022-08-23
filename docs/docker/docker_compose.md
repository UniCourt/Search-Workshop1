### What is Docker Compose
Developing applications using Docker can become challenging when juggling multiple services and containers.<br>
Docker Compose is the tool that will help you define and run multi-container Docker applications.<br>

An application can consist of multiple containers running different services. It can be tedious to start and 
manage containers manually, so Docker created a useful tool that helps speed up the process - Docker Compose.
<br>

Docker Compose works by applying rules defined in a docker-compose.yaml file. The YAML file configures the 
application's services and includes rules specifying how you want them to run. With the file in place, you can start, 
stop, or rebuild all the services using a single command. Additionally, you can check the status of a service, 
display log outputs, and run one-off commands.

### Docker Compose Basic Commands

```commandline
Command	Description
docker-compose --help	Get help on a command
docker-compose build	Look for all services containing the build: statement in the docker-compose.yml file and run a docker build for each one
docker-compose run	Run a one-off command
docker-compose up	Create and start containers
docker-compose -f 	Specify the name and path of one or more Compose files
docker-compose start	Start existing containers for a service
docker-compose stop	Stop running containers (without removing them)
docker-compose pause	Pause running containers of a service
docker-compose unpause	Unpause paused containers of a service
docker-compose down	Stop containers (and remove containers, networks, volumes, and images)
docker-compose ps	List containers within the docker-compose configuration file
docker-compose images	List images used by created containers
docker-compose ls	List running Compose projects
```

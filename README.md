# Git, Docker and Postgres Workshop
Testing
One Day workshop on understanding Git, Docker and Postgres

## Prerequisite

##### Any Linux machine with following packages installed
- git
- python3.10
- Docker
- Docker Compose

##### GitHub account
- Create an account on [GitHub](https://github.com/join) (if you don't already have one)
- Fork [this](https://github.com/UniCourt/Search-Workshop1) repository and then clone it to your machine
- You can refer [this](https://docs.github.com/en/get-started/quickstart/fork-a-repo) guide to understand how to fork and clone


##### Docker
- To install docker go to your cloned repository and run the following command
- `sudo sh install_docker.sh`

## What will you learn by the end of this workshop?
- Introduction to GIT
- Git commands (push, pull make Pull request etc)
- Concepts of containerisation and why its required.
- Building and running your own Containers.
- Running Multiple Services with Docker Compose
- Other docker concepts like exposing Ports, Volume Mounts, Utilizing Networks, Limiting Resources (the 4 features we use regularly.)
- Basics of postgres.
- Connecting and querying to postgres database.
- Integration of scripts and postgres as multiple services as containers.
- Reading data from files and populating to database.

## Schedule
| Time            | Topics
|-----------------|-------
| 09:00 - 9:15   |  `Introduction`
| 09:15 - 10:00   |  [`Introduction to GIT`](docs/git/git_intro.md)
| 9:45 - 10:15   |  [`Git Commands (push, pull, make Pull request etc)`](docs/git/git.md)
| 10:15 - 10:30   |  [`What is docker`](docs/docker/docker_intro.md)
| 10:30 - 11:30   |  [`Docker Commands`](docs/docker/docker_commands.md)
| 11:45 - 12:00    | [`Run Multiple Services with Docker Compose`](docs/docker/docker_compose.md)
| 12:00 -  12:30  |  [`Expose Ports, Volume Mounts, Utilizing Networks, Limiting Resources`](docs/docker/docker_volume_mount.md)
| 12:30 - 1:00   | [`Introduction to Postgres`](docs/postgres/README.md)
| 01:00 - 02:00   |  `Break`
| 2:00 -  2:30  |  [`Docker compose with Postgres`](docs/script/script_1.md)
| 2:00 -  2:30    |  `Postgres Continuation`
| 2:30 -  4:00    |  [`Running scripts`](docs/script/script_2.md)
| 4:00 -  4:30    |  `Q & A and Wrapping Up`

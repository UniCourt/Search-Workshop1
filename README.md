# Git, Docker and Postgres Workshop

One Day workshop on understanding Git, Docker and Postgres

## Prerequisite
### Linux machine with following packages installed
  1. Install Ubuntu 20.04.2 LTS.
  2. Install Git from your terminal by running following commands
     -   ```
         sudo apt-get update
         ```
     -   ```
         sudo apt-get install git
         ```
  3. Verify the installation was successful by typing
     -   ```
         git --version

### Fork and clone the workshop project from github:
 a. Log into your github account: https://github.com/ 

 b. After installing git, to start using git from your computer, you must enter your credentials to identify yourself as the author of your work. The username and email address should match the ones you use in Github.

Add your username: 

     git config --global user.name "your_username"


Add your email address:

    git config --global user.email "your_email_address@example.com"

To check the configuration, run:

    git config --global --list

Add ssh keys to your GitHub account:

    1. ssh-keygen -t ed25519 -C  "your_email"
    2. cat ~/.ssh/id_ed25519.pub
    3. Visit this url: https://github.com/settings/ssh/new. Paste the key and save.

### c. Fork the repository
Forking refers to making a copy of a project you want to contribute to. 
Now lets fork a project provided to complete this activity. 

Follow these steps to fork a project:

1. Go to the project url using this link: https://github.com/UniCourt/Search-Workshop1
2. Click on the fork button in the project page
3. Select a namespace to fork the project.


#### d. Clone the repository
Cloning a repository means the files from the remote repository are downloaded to your computer, 
and a connection is created.

1. Go to your project’s landing page and click Clone.
2. Copy the URL for Clone with SSH.
3. Open a terminal and go to the directory where you want to clone the files. Run these commands: \
i.  ```cd``` \
ii. ```mkdir projects``` \
iii.```cd projects``` \
iv. ```git clone <url_to_clone>``` 

### 3. Install Docker:
```cd ~/projects/Search-Workshop1```\
```sudo sh install_docker.sh```

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
test

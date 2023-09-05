## Running scripts using postgres
We will be running postgres queries using a script.


### Build script docker image
###### Note: Please make the following changes in the Dockerfile 
```
ENV POSTGRES_HOST='127.0.0.1'
In the above line replace '127.0.0.1' with your local system ip
```
```
cd Search-Workshop1
docker build -t "ws1-script2" .
```

### Bring up script container.
```
docker run -it ws1-script2:latest bash
```

### Running script container

1. Login to postgres
```
psql -U postgres --host <system_ip> --port 5435
\q
```
######Note -> password - postgres

2. Create database 
```
CREATE DATABASE amazon;
\q
```

3. Dump schema.sql file to amazon database
```
psql -U postgres -d amazon --host <system_ip> --port 5435 < src/schema/schema.sql
```

4. Run the script
```
cd src/app
python3 populate.py
```



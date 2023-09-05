## Running scripts using docker compose
We will be getting up Postgres and a simple script to run as containers using docker compose.


### Run Docker Compose
```
cd Search-Workshop1
docker-compose up
```

### Working with database.
1. Login to database container.
```
docker exec -it ws1_db sh
```

2. Login to postgres
```
psql -U postgres
```

3. Create a database
```
CREATE DATABASE student;
\q
```

4. Dump student.sql file to student database
```
psql -U postgres -d student < sql_file/student.sql
```

### Running script
1. Login to script container.
```
docker exec -it ws1_script sh
```

2. Run script:
```
python3 script.py 
```

FROM python

RUN apt-get update && apt-get install -y postgresql-client
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ENV POSTGRES_DB='amazon'
ENV POSTGRES_USER='workshop_user'

ENV POSTGRES_PASSWORD='workshop_user1'

ENV POSTGRES_HOST='127.0.0.1'

ENV POSTGRES_PORT='5435'
COPY ./ ./

FROM public.ecr.aws/docker/library/python

RUN apt-get update && apt-get install -y postgresql-client
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ENV POSTGRES_DB='amazon'
ENV POSTGRES_USER='workshop_user'

ENV POSTGRES_PASSWORD='workshop_user1'

ENV POSTGRES_HOST='172.20.3.85'

ENV POSTGRES_PORT='5435'
COPY ./ ./

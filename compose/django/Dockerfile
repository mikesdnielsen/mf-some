FROM python:3.6.4
ENV PYTHONBUFFERED 1
ARG ISTEST=0

RUN apt-get update && apt-get install -y gettext

RUN pip install --upgrade pip setuptools wheel

COPY ./requirements /requirements
RUN /bin/bash -c 'pip install -r /requirements/local.txt'

COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/django/start-dev.sh /start-dev.sh
RUN chmod +x /start-dev.sh


RUN mkdir /code
WORKDIR /code
ADD mf_some /code

ENTRYPOINT ["/entrypoint.sh"]

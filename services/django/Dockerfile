# Drumrose Front-end
# Version: 1.0
FROM ubuntu:18.04
LABEL Maintainer="Jason Brill <jason@drumrose.com>"

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /usr/local/drumrose/services/django

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    make \
    curl \
    sudo \
    vim

# -- Install Pipenv:
RUN apt update && apt upgrade -y && apt install python3.7-dev libffi-dev -y && apt install python3-distutils -y && apt-get install -y netcat
RUN curl --silent https://bootstrap.pypa.io/get-pip.py | python3.7

# Backwards compatility.
RUN rm -fr /usr/bin/python3 && ln /usr/bin/python3.7 /usr/bin/python3

RUN pip3 install pipenv

# Link python -> python3
RUN alias python=python3

# Postgres client
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/local/drumrose/

WORKDIR /usr/local/drumrose/

COPY . /usr/local/drumrose/

# install python packages
RUN pipenv install --dev --system --deploy

RUN chmod +x django_entry.sh 

EXPOSE 8000

ENTRYPOINT [ "./django_entry.sh" ]
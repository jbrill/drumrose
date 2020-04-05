FROM ubuntu:18.04
LABEL Maintainer="Jason Brill <jlbrill@umich.edu>"
# Neptune API
# Version: 1.0

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Python, don't write bytecode!
ENV PYTHONDONTWRITEBYTECODE 1

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN apt-get install -y \
    curl \
    sudo \
    vim

# -- Install Pipenv:
RUN apt update && apt upgrade -y && apt install python3.7-dev libffi-dev -y && apt install python3-distutils -y

RUN curl --silent https://bootstrap.pypa.io/get-pip.py | python3.7

# Backwards compatility.
RUN rm -fr /usr/bin/python3 && ln /usr/bin/python3.7 /usr/bin/python3

RUN pip3 install pipenv

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/drumrose/django
COPY . /usr/local/drumrose/django/
RUN pipenv install --system --deploy

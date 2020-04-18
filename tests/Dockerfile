FROM ubuntu:18.04

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /usr/local/drumrose

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    curl \
    sudo \
    vim \
    make

# -- Install Pipenv:
RUN apt update && apt upgrade -y && apt install python3.7-dev libffi-dev -y && apt install python3-distutils -y
RUN curl --silent https://bootstrap.pypa.io/get-pip.py | python3.7

# Backwards compatility.
RUN rm -fr /usr/bin/python3 && ln /usr/bin/python3.7 /usr/bin/python3

RUN pip3 install pylint pylint-django

WORKDIR /usr/local/drumrose
COPY . /usr/local/drumrose

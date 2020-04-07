FROM ubuntu:18.04
LABEL Maintainer="Jason Brill <jlbrill@umich.edu>"
# Drumrose Front-end
# Version: 1.0

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    curl \
    sudo \
    vim \
    nodejs \
    npm

# Project Files and Settings
ARG PROJECT=neptune-nuxt
ARG PROJECT_DIR=/var/www/${PROJECT}
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
RUN ls
COPY package.json package-lock.json ./

<<<<<<< HEAD:services/neptune-nuxt/Dockerfile
RUN npm install --verbose
=======
RUN sudo apt-get install -y nodejs

RUN mkdir -p /usr/local/drumrose/services/nuxt/

WORKDIR /usr/local/drumrose/services/nuxt/

<<<<<<< HEAD
RUN npm install
>>>>>>> dc9f6e5... Nomenclature changes:services/nuxt/Dockerfile
=======
COPY . /usr/local/drumrose/services/nuxt/
RUN npm ci
>>>>>>> b6bea85... (feature) scrap auth

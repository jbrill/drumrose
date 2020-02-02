FROM ubuntu:16.04
LABEL Maintainer="Jason Brill <jlbrill@umich.edu>"
# Neptune Front-end
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

RUN npm install --verbose

# Drumrose Front-end
# Version: 1.0
FROM ubuntu:18.04
LABEL Maintainer="Jason Brill <jason@drumrose.com>"

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

RUN mkdir -p /usr/local/drumrose/

WORKDIR /usr/local/drumrose/

<<<<<<< HEAD
<<<<<<< HEAD
RUN npm install
>>>>>>> dc9f6e5... Nomenclature changes:services/nuxt/Dockerfile
=======
COPY . /usr/local/drumrose/services/nuxt/
<<<<<<< HEAD
RUN npm ci
>>>>>>> b6bea85... (feature) scrap auth
=======

# CI=1 to not ignore tty output
RUN CI=1 npm ci
>>>>>>> 771fa62... (feature) cypress
=======
COPY . /usr/local/drumrose/

EXPOSE 3000

# CI=1 to not ignore tty output
RUN CI=1 npm ci

CMD ["npm", "run", "dev"]
>>>>>>> 107887a... create different environment pipeline

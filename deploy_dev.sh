#!/bin/sh

ssh -o StrictHostKeyChecking=no root@$DIGITAL_OCEAN_IP_ADDRESS << 'ENDSSH'
  cd /drumrose
  export $(cat .django.env | xargs)
  export $(cat .nuxt.env | xargs)
  export $(cat .nginx.env | xargs)
  docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  docker pull registry.gitlab.com/jbrill/drumrose/django-server:dev
  docker pull registry.gitlab.com/jbrill/drumrose/nuxt-server:dev
  docker pull registry.gitlab.com/jbrill/drumrose/nginx-server:dev
  git fetch
  git checkout $CI_COMMIT_SHA
  docker-compose -f docker-compose.deploy-dev.yml up -d
  chmod +x ./scripts/wait_till_container_healthy.sh
  ./scripts/wait_till_container_healthy.sh drumrose_django-server_1
  ./scripts/wait_till_container_healthy.sh drumrose_nuxt-server_1
ENDSSH
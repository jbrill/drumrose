#!/bin/sh

ssh -o StrictHostKeyChecking=no drumrose@$DIGITAL_OCEAN_PROD_IP_ADDRESS << 'ENDSSH'
  cd drumrose
  docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  docker pull registry.gitlab.com/jbrill/drumrose/django-server:prod
  docker pull registry.gitlab.com/jbrill/drumrose/nuxt-server:prod
  docker pull registry.gitlab.com/jbrill/drumrose/nginx-server:prod
  git fetch
  git checkout $CI_COMMIT_SHA
  docker-compose -f docker-compose.deploy-prod.yml up -d
  chmod +x ./scripts/wait_till_container_healthy.sh
  ./scripts/wait_till_container_healthy.sh drumrose_django-server_1
ENDSSH
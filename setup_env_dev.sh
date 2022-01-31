#!/bin/bash

rm .django.env 2> /dev/null
echo POSTGRES_DB_NAME=$POSTGRES_DB_NAME >> .django.env
echo POSTGRES_USER=$POSTGRES_USER >> .django.env
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> .django.env
echo POSTGRES_HOST=$POSTGRES_HOST >> .django.env
echo POSTGRES_PORT=$POSTGRES_PORT >> .django.env
echo DRUMROSE_PATH=$DRUMROSE_PATH >> .django.env
echo APPLE_MUSIC_SECRET=$APPLE_MUSIC_SECRET >> .django.env
echo APPLE_MUSIC_KEY_ID=$APPLE_MUSIC_KEY_ID >> .django.env
echo APPLE_MUSIC_TEAM_ID=$APPLE_MUSIC_TEAM_ID >> .django.env
echo AUTH0_CLIENT_ID=$AUTH0_CLIENT_ID >> .django.env
echo AUTH0_CLIENT_SECRET=$AUTH0_CLIENT_SECRET >> .django.env
echo AUTH0_AUDIENCE=$AUTH0_AUDIENCE >> .django.env
echo AUTH0_DOMAIN=$AUTH0_DOMAIN >> .django.env
echo SECRET_KEY=$SECRET_KEY >> .django.env
echo DJANGO_ALLOWED_HOSTS=$DJANGO_ALLOWED_HOSTS >> .django.env
echo DEBUG=$DEBUG >> .django.env
echo DATABASE=$DATABASE >> .django.env
echo CI_REGISTRY_USER=$CI_REGISTRY_USER >> .django.env
echo CI_REGISTRY_PASSWORD=$CI_REGISTRY_PASSWORD >> .django.env
echo CI_REGISTRY=$CI_REGISTRY >> .django.env
echo CI_COMMIT_SHA=$CI_COMMIT_SHA >> .django.env

rm .nginx.env 2> /dev/null
echo DRUMROSE_DOMAIN=$DRUMROSE_DOMAIN >> .nginx.env

rm .nuxt.env 2> /dev/null
echo NODE_ENV=$NODE_ENV >> .nuxt.env
echo AUTH0_CLIENT_ID=$AUTH0_CLIENT_ID >> .nuxt.env
echo AUTH0_DOMAIN=$AUTH0_DOMAIN >> .nuxt.env
echo API_AUDIENCE=$API_AUDIENCE >> .nuxt.env
echo DOMAIN_HOST=$DOMAIN_HOST >> .nuxt.env
echo SENTRY_DSN=$SENTRY_DSN >> .nuxt.env
echo NUXT_PORT=3001 >> .nuxt.env

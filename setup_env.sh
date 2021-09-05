#!/bin/bash

# django dev env
echo API_URL=$API_URL >> .django.dev.env
echo NODE_ENV=$NODE_ENV >> .django.dev.env
echo POSTGRES_DB_NAME=$POSTGRES_DB_NAME >> .django.dev.env
echo POSTGRES_USER=$POSTGRES_USER >> .django.dev.env
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> .django.dev.env
echo POSTGRES_HOST=$POSTGRES_HOST >> .django.dev.env
echo POSTGRES_PORT=$POSTGRES_PORT >> .django.dev.env
echo DRUMROSE_PATH=$DRUMROSE_PATH >> .django.dev.env
echo APPLE_MUSIC_SECRET=$APPLE_MUSIC_SECRET >> .django.dev.env
echo APPLE_MUSIC_KEY_ID=$APPLE_MUSIC_KEY_ID >> .django.dev.env
echo APPLE_MUSIC_TEAM_ID=$APPLE_MUSIC_TEAM_ID >> .django.dev.env
echo AUTH0_CLIENT_ID=$AUTH0_CLIENT_ID >> .django.dev.env
echo AUTH0_CLIENT_SECRET=$AUTH0_CLIENT_SECRET >> .django.dev.env
echo AUTH0_AUDIENCE=$AUTH0_AUDIENCE >> .django.dev.env
echo AUTH0_DOMAIN=$AUTH0_DOMAIN >> .django.dev.env
echo SECRET_KEY=$SECRET_KEY >> .django.dev.env
echo DJANGO_ALLOWED_HOSTS=$DJANGO_ALLOWED_HOSTS >> .django.dev.env
echo DEBUG=$DEBUG >> .django.dev.env
echo DATABASE=$DATABASE >> .django.dev.env

# nuxt dev env
echo AUTH0_CLIENT_ID=$AUTH0_CLIENT_ID >> .nuxt.dev.env
echo AUTH0_DOMAIN=$AUTH0_DOMAIN >> .nuxt.dev.env
echo API_AUDIENCE=$API_AUDIENCE >> .nuxt.dev.env
echo DOMAIN_HOST=$DOMAIN_HOST >> .nuxt.dev.env
echo SENTRY_DSN=$SENTRY_DSN >> .nuxt.dev.env

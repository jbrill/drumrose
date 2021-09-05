#!/bin/bash

# django dev env
echo POSTGRES_DB_NAME=drumrose_db >> .django.dev.env
echo POSTGRES_USER=drumrose_user >> .django.dev.env
echo POSTGRES_PASSWORD=drumrose_password >> .django.dev.env
echo POSTGRES_HOST=postgres-server >> .django.dev.env
echo POSTGRES_PORT=5432 >> .django.dev.env
echo DRUMROSE_PATH=/usr/local/drumrose >> .django.dev.env
echo APPLE_MUSIC_SECRET=-----BEGIN PRIVATE KEY-----\nMIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgHeM2ZFBsXRnd0PlN\n9svOLOCc04mWieDDRzLo7/jgDwSgCgYIKoZIzj0DAQehRANCAAQYI4OAa+ck3ZPf\nuQJLKxCEZQ8Nm92YhjMw5yLZ5iALR6/d3X8W4TuDdi+NviKpWDBnkFcgVXqmQAIS\nOMEVWyIJ\n-----END PRIVATE KEY----- >> .django.dev.env
echo APPLE_MUSIC_KEY_ID=C3A37KT32B >> .django.dev.env
echo APPLE_MUSIC_TEAM_ID=PYME62NVGN >> .django.dev.env
echo AUTH0_CLIENT_ID=ApqgC9UHWyDV0Qb6rv3cby0gP47u5ZmO >> .django.dev.env
echo AUTH0_CLIENT_SECRET=https://drumrose.auth0.com/api/v2/ >> .django.dev.env
echo AUTH0_AUDIENCE=https://drumrose.auth0.com/api/v2/ >> .django.dev.env
echo AUTH0_DOMAIN=https://drumrose.auth0.com >> .django.dev.env
echo SECRET_KEY=n467bz@g24axx$=zf17ty@$j(m!t9o+tu!lhfafd4$_!r7ja&$ >> .django.dev.env
echo DJANGO_ALLOWED_HOSTS=localhost django-server 127.0.0.1 [::1] >> .django.dev.env
echo DATABASE=postgres >> .django.dev.env

# nuxt dev env
echo NODE_ENV=development >> .nuxt.dev.env
echo AUTH0_CLIENT_ID=nA1RUMeTG88LVxGeEJc9Xu4PhWPHQRTg >> .nuxt.dev.env
echo AUTH0_DOMAIN=drumrose.auth0.com >> .nuxt.dev.env
echo API_AUDIENCE=https://teton.drumrose.io >> .nuxt.dev.env
echo DOMAIN_HOST=https://teton.drumrose.io >> .nuxt.dev.env
echo SENTRY_DSN=https://32b5cda72cf2429ea4e26a531dde7ae3@o419445.ingest.sentry.io/5332895 >> .nuxt.dev.env

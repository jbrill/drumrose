#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate --noinput  || exit 1

# Import fixtures
# echo "Loading dev fixtures"
# python3 manage.py loaddata api/fixtures/data.json
gunicorn api.wsgi:application --bind 0.0.0.0:8000 --capture-output

exec "$@"
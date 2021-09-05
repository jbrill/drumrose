#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

# Import fixtures
echo "Loading dev fixtures"
#python3 manage.py loaddata api/fixtures/data.json

exec "$@"
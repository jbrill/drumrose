#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

# Import fixtures
echo "Loading dev fixtures"
#python3 manage.py loaddata api/fixtures/data.json

# Start server
echo "Starting server"
python3 manage.py runserver 0.0.0.0:8000

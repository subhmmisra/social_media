#!/bin/sh

# Apply database migrations
python manage.py migrate

# Start the Django development server
exec "$@"

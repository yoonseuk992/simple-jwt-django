#!/usr/bin/env sh

# Start Gunicorn processes

exec gunicorn --env DJANGO_SETTINGS_MODULE=simple_jwt.settings simple_jwt.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1 \
    --log-level=info \
    --log-file=-



#!/bin/bash
poetry shell

python manage.py collectstatic --clear --noinput

cp -r /app/collected_static/. /backend_static/static/

gunicorn nalog.wsgi:application --bind 0.0.0.0:8000

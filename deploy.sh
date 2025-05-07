#!/bin/bash
# Install dependencies
pip install -r requirements.txt
# Run migrations
python manage.py migrate
# Collect static files (if needed)
python manage.py collectstatic --noinput
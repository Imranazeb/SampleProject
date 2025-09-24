#!/bin/bash

set -o errexit

set -o pipefail

set -o nounset

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input

#create superuser if not exists with email admin@example.com and password admin1234
# If the user already exists, ignore the error
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='admin@example.com').exists() or User.objects.create_superuser(username='admin', email='admin@example.com', password='admin123')" | python manage.py shell


python manage.py runserver 0.0.0.0:8000
import os

from celery import Celery
from django.conf import settings

if os.getenv('DOCKER', False):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings.local')
    app = Celery('app') # TODO define app here
    app.config_from_object('django.conf:settings', namespace='CELERY')
    app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

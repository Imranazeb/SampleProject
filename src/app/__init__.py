import os

if os.getenv('DOCKER', False):
    from .celery import app as celery_app
    __all__ = ('celery_app',)
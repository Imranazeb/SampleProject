from .base import * # noqa

env_file = BASE_DIR / '../.environment/.env.dev'
env = environ.Env()
env.read_env(env_file)

SECRET_KEY = getenv('SECRET_KEY')
DEBUG = bool(int(getenv('DEBUG', default=0)))

ALLOWED_HOSTS = list(filter(None, getenv('ALLOWED_HOSTS', '').split(',')))
CSRF_TRUSTED_ORIGINS = list(filter(None, getenv('CSRF_TRUSTED_ORIGINS', '').split(',')))

DOCKER= getenv("DOCKER", default=False)

ADMIN_URL = getenv("ADMIN_URL", default="admin/")

LOCAL_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DOCKER_DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv("POSTGRES_DB"),
        "USER": getenv("POSTGRES_USER"),
        "PASSWORD": getenv("POSTGRES_PASSWORD"),
        "HOST": getenv("POSTGRES_HOST"),
        "PORT": getenv("POSTGRES_PORT"),
    }
}

DATABASES = DOCKER_DATABASES if DOCKER else LOCAL_DATABASES
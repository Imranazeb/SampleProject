from .base import *  # noqa

env_file = BASE_DIR / "../.environment/.env.dev"
env = environ.Env()
env.read_env(env_file)

SECRET_KEY = getenv("SECRET_KEY")
DEBUG = bool(int(getenv("DEBUG", default=0)))

ALLOWED_HOSTS = list(filter(None, getenv("ALLOWED_HOSTS", "").split(",")))
CSRF_TRUSTED_ORIGINS = list(filter(None, getenv("CSRF_TRUSTED_ORIGINS", "").split(",")))

DOCKER = getenv("DOCKER", default=False)

ADMIN_URL = getenv("ADMIN_URL", default="admin/")

# DATABASES

LOCAL_DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
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


# Mail-Hog Setup
if DOCKER:
    getenv("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
    EMAIL_HOST = getenv("EMAIL_HOST", default="mailhog")
    EMAIL_PORT = int(getenv("EMAIL_PORT", default=1025))

if not DOCKER:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

# CELERY
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BROKER_URL = getenv("CELERY_BROKER")
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
CLEREY_TASK_SEND_SENT_EVENT = True

CELERY_RESULT_BACKEND = getenv("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_RESULT_BACKEND_MAX_RETRIES = 10

CELERY_TASK_SEND_SENT_EVENT = True
CELERY_RESULT_EXTENDED = True
CELERY_RESULT_BACKEND_ALWAYS_RETRY = True
CELERY_TASK_TIME_LIMIT = 5 * 60
CELERY_TASK_SOFT_TIME_LIMIT = 60
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_WORKER_SEND_TASK_EVENTS = True
CELERY_BEAT_SCHEDULE = {}
# CELERY_BEAT_SCHEDULE = {
#     "run-test-task-10-seconds": {
#         "task": "common.core.tasks.test_task",
#         "schedule": 10.0,
#     },
# }
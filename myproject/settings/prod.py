from .base import *
from decouple import config

DEBUG = False
ALLOWED_HOSTS = ["portfolio-project-jepp.onrender.com"]

DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'), conn_max_age=600)
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config('CACHE_URL'),
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

CELERY_BROKER_URL = config('BROKER_URL')
CELERY_RESULT_BACKEND = config('BROKER_URL')

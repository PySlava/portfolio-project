from decouple import Config, RepositoryEnv
from .base import *

config = Config(RepositoryEnv(BASE_DIR / '.env'))

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
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

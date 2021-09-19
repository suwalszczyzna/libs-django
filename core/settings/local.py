from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'libs',
        'USER': 'libs',
        'PASSWORD': 'libs',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

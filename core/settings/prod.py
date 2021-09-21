from .base import *
import django_heroku

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('POSTGRES_NAME'),
        'USER': get_env_variable('POSTGRES_USER'),
        'PASSWORD': get_env_variable('POSTGRES_PASSWORD'),
        'HOST': get_env_variable('POSTGRES_HOST'),
        'PORT': get_env_variable('POSTGRES_PORT'),
    }
}

django_heroku.settings(locals())
ALLOWED_HOSTS = [
    'libs-django.herokuapp.com',
    'daemon-libs.netlify.app'
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'https://daemon-libs.netlify.app',
]

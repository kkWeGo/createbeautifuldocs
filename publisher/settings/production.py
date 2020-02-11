from .base import *
import dj_database_url
import django
import psycopg2

ENVIRONMENT = 'production'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dc6998hfm9pefm',
        'USER': 'sfaaadipuwcvoi',
        'PASSWORD': '98c7af63806a5409eb0dea2e9eb8add4430a283e7d11f0a72697028fa1e2042c',
        'HOST': 'ec2-46-137-156-205.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}

django.setup()

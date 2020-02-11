from .base import *
import dj_database_url
import django

ENVIRONMENT = 'production'
DEBUG = True
ALLOWED_HOSTS = ['createbeautifuldocs.herokuapp.com']
DATABASES['default'] = dj_database_url.config(
    default='postgres://sfaaadipuwcvoi:98c7af63806a5409eb0dea2e9eb8add4430a283e7d11f0a72697028fa1e2042c@ec2-46-137-156-205.eu-west-1.compute.amazonaws.com:5432/dc6998hfm9pefm'
)
django.setup()

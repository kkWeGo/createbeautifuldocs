from .base import *
import dj_database_url
import django

ENVIRONMENT = 'production'
DEBUG = True
ALLOWED_HOSTS = ['createbeautifuldocs.herokuapp.com']
DATABASES['default'] = dj_database_url.config(
    default='postgres://wdtktiblvnhkzz:8e5a9fd91df352a0718334c3a5f33eb59eeb30dad1bfa5e0c17b3080ec9a40d0@ec2-184-72-235-80.compute-1.amazonaws.com:5432/d8mshascf4h594'
)
#DATABASES = {
 #   'default': 
 #       dj_database_url.config(
 #           'postgres://rzbuurxglahzlw:a8f18093a4f3d1bdd25498981c69fc5e9ef6bd0a829d2a40383ea65a7affddda@ec2-34-197-171-33.compute-1.amazonaws.com:5432/dl9ab8mrb9kbo'
  #      )
#}
django.setup()

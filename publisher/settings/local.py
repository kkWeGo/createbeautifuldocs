from .base import *
import django

ENVIRONMENT = 'local'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev_db.sqlite3'),
    }
}

django.setup()
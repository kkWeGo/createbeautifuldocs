web: gunicorn publisher.wsgi --log-file -
worker: celery worker -A publisher -E -l debug
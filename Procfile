web: gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker
release: python manage.py migrate
worker: celery worker --app=config.celery_app --loglevel=info
beat: celery beat --app=config.celery_app --loglevel=info

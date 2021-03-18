gunicorn run:flask_app -b 0.0.0.0:5000 --worker-class=eventlet --timeout 120 & celery -A app.task:celery worker -l info & celery -A app.task:celery beat -s "celerybeat-async_task" --pidfile=

python run.py & celery -A app.task:celery worker -l info & celery -A app.task:celery beat -s "celerybeat-async_task" --pidfile=

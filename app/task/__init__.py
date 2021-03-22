from celery import Celery

from app.setting import config

# celery = Celery('app.task', broker=Config.CELERY_BROKER_URL, result_backend=Config.CELERY_RESULT_BACKEND, )
celery = Celery()
celery.conf.timezone = 'Asia/Shanghai'
celery.autodiscover_tasks(['app.task.timed_task'])
celery.config_from_object(config)

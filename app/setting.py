from celery.schedules import crontab


class ConfigDev:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../data'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BROKER_URL = 'redis://172.16.100.10:6379/0'
    CELERYBEAT_SCHEDULE = {
        'collect_course_data': {
            'task': 'app.task.timed_task.collect_course_data',
            'schedule': crontab(minute=30, hour=23),
            'args': ()
        },
    }


class ConfigProd:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../data'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BROKER_URL = 'redis://127.0.0.1:6379/0'
    CELERYBEAT_SCHEDULE = {
        'collect_course_data': {
            'task': 'app.task.timed_task.collect_course_data',
            'schedule': crontab(minute=30, hour=23),
            'args': ()
        },
    }


Config = ConfigDev





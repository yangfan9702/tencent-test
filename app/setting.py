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

    ELASTIC_APM = {
        'SERVICE_NAME': 'tencent-test',
        'SECRET_TOKEN': '',
        'SERVER_URL': 'http://172.16.100.11:8200',
        'DEBUG': True
    }


class ConfigProd:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../data'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BROKER_URL = 'redis://172.16.100.11:6379/0'
    CELERYBEAT_SCHEDULE = {
        'collect_course_data': {
            'task': 'app.task.timed_task.collect_course_data',
            'schedule': crontab(minute=30, hour=23),
            'args': ()
        },
    }

    ELASTIC_APM = {
        'SERVICE_NAME': 'tencent-test',
        'SECRET_TOKEN': '',
        'SERVER_URL': 'http://172.16.100.11:8200',
        'DEBUG': True
    }


config = ConfigDev()





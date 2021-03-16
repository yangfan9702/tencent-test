"""
定时任务
"""
import requests
from datetime import datetime
from bs4 import BeautifulSoup

from app.model import db, Course, CourseCount
from . import celery


@celery.task()
def collect_course_data():
    from app import flask_app
    from flask import current_app

    with flask_app.app_context():
        all_course = Course.query.filter_by().all()
        for course in all_course:
            course_url = f'https://ke.qq.com/course/list?mt=1001&st={course.st}&tt={course.tt}'
            url = course_url + '&page={page}'
            resp = requests.get(url.format(page=1))
            if resp.status_code != 200:
                return
            count = 0
            # 页数
            _html = BeautifulSoup(resp.text, features='html.parser')
            page_num = _html.find_all('a', class_='page-btn')[-1].text if _html.find_all('a', class_='page-btn') else 1
            count += 20 * (int(page_num)-1)
            # 最后一页数量
            resp = requests.get(url.format(page=page_num))
            _html = BeautifulSoup(resp.text, features='html.parser')
            current_page_size = len(_html.find_all('li', class_='js-course-card-item'))
            count += current_page_size

            course_count = CourseCount(course_id=course.id, count=count, update_at=datetime.now().date())
            db.session.add(course_count)
            db.session.commit()

        current_app.logger.info('collect_course_data done.')


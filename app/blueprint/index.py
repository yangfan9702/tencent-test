from flask import Blueprint, g
from sqlalchemy import func
from jinja2 import Markup
import pyecharts.options as opts
from pyecharts.charts import Line
from app.task.timed_task import collect_course_data

from app.model import db, Course, CourseCount

index_bp = Blueprint('index', __name__)


@index_bp.route('/', methods=['GET'])
def index():
    date_ = db.session.query(
        func.distinct(CourseCount.update_at).label('update_at')
    ).order_by(
        CourseCount.update_at.asc()  # noqa
    ).all()

    name_ = db.session.query(
        Course.name
    ).order_by(
        Course.id.asc()  # noqa
    ).all()

    course_count_ = db.session.query(
        CourseCount.count,
        CourseCount.update_at,
        Course.name
    ).join(
        Course,
        CourseCount.course_id == Course.id
    ).order_by(
        CourseCount.update_at.asc(),  # noqa
        CourseCount.course_id.asc()  # noqa
    ).all()

    x_date = [_.update_at for _ in date_]
    y_name = [_.name for _ in name_]
    data = []
    for name in y_name:
        d = list()
        for course_count in course_count_:
            if course_count.name == name:
                d.append(course_count.count)
        data.append((name, d))

    c = Line().add_xaxis(x_date).set_global_opts(
        title_opts=opts.TitleOpts(title="腾讯课堂-课程数量走势")
    )
    for d in data:
        c.add_yaxis(
            d[0], d[1], is_connect_nones=True
        )
    return Markup(c.render_embed())


@index_bp.route('/test_apm', methods=['GET'])
def test_apm():
    from app import apm
    try:
        1 / 0
    except ZeroDivisionError:
        apm.capture_message('caught a zero division error')
        apm.capture_exception()


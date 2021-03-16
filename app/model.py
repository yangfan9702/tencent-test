from sqlalchemy import Column, Date, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()
metadata = Base.metadata


class Course(db.Model):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    st = Column(Integer)
    tt = Column(Integer)
    name = Column(Text(32))


class CourseCount(db.Model):
    __tablename__ = 'course_count'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer)
    count = Column(Integer)
    update_at = Column(Date)

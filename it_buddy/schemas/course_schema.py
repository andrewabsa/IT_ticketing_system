from main import ma
from models.courses import Course
from marshmallow_sqlalchemy import auto_field

class CourseSchema(ma.SQLAlchemyAutoSchema):
    course id = auto_field(dump_only=True)

    class Meta:
        model = Course
        load_instance = True
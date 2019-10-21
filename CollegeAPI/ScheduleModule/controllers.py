from CollegeAPI import db
from .models import Schedule
from ..CourseModule.controllers import Course_detail
from ..CourseModule.models import CourseSchema
from flask import jsonify, request, Blueprint
from sqlalchemy import and_


Courses_Schema = CourseSchema(many=True)
app = Blueprint('ScheduleModule', __name__)


@app.route("/schedule", methods=["POST"])
def add_Schedule():
    StudentID = request.json['StudentID']
    CourseID = request.json['CourseID']

    new_Schedule = Schedule(StudentID, CourseID)

    db.session.add(new_Schedule)
    db.session.commit()

    return jsonify(True)

#Endpoint to show specific Schedules
@app.route("/schedule/<StudentID>", methods=["GET"])
def get_Schedule(StudentID):
    all_Schedules = Schedule.query.filter(Schedule.StudentID == StudentID)
    resultSchedules = Courses_Schema.dump(all_Schedules)
    All_Courses = []
    for Course in resultSchedules:
        All_Courses.append(Course_detail(Course['CourseID']))

    result = Courses_Schema.dump(All_Courses)
    return jsonify(result)

@app.route("/schedule/<StudentID>/<CourseID>", methods=["DELETE"])
def Schedule_delete(StudentID, CourseID):
    Schedules = Schedule.query.filter(and_(Schedule.CourseID == CourseID, Schedule.StudentID == StudentID)).first()
    db.session.delete(Schedules)
    db.session.commit()

    return jsonify(True)
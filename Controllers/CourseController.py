from CollegeAPI import db, app
from Models.Course import Course,CourseSchema
from flask import jsonify,request

Course_Schema = CourseSchema
Courses_Schema = CourseSchema(many=True)

def CourseGet(CourseID):
    Course = Course.query.filter(Course.CourseID == CourseID).first()
    return Course
#endpoint for new Course
@app.route("/Course", methods = ["POST"])
def add_Course():
    CourseName = request.json['CourseName']
    CourseID = request.json['CourseID']
    CourseSection = request.json['CourseSection']
    CourseRoom = request.json['CourseRoom']
    ScheduleDays = request.json['ScheduleDays']
    ScheduleHours = request.json['ScheduleHours']
    CourseTeacher = request.json['CourseTeacher']

    new_Course = Course(CourseName,CourseID,CourseSection,CourseRoom,ScheduleDays,ScheduleHours,CourseTeacher)

    db.session.add(new_Course)
    db.session.commit()

    return Course_Schema.jsonify(new_Course)

#Endpoint to show all Courses
@app.route("/Course", methods=["GET"] )
def get_Course():
    all_Courses = Course.query.all()
    result = Courses_Schema.dump(all_Courses)
    return jsonify(result)

#Endpoint to show detail of a Course by CourseID
@app.route("/Course/<CourseID>", methods=["GET"])
def Course_detail(CourseID):
    Course = Course.query.filter(Course.CourseID == CourseID).first()
    return Course_Schema.jsonify(Course)


# endpoint to update Course
@app.route("/Course/<CourseID>", methods=["PUT"])
def Course_update(CourseID):
    Course = Course.query.filter(Course.CourseID == CourseID).first()
    CourseName = request.json['CourseName']
    CourseID = request.json['CourseID']
    CourseSection = request.json['CourseSection']
    CourseRoom = request.json['CourseRoom']
    ScheduleDays = request.json['ScheduleDays']
    ScheduleHours = request.json['ScheduleHours']
    CourseTeacher = request.json['CourseTeacher']

    Course.CourseName = CourseName
    Course.CourseID = CourseID
    Course.CourseSection = CourseSection
    Course.CourseRoom = CourseRoom
    Course.ScheduleDays = ScheduleDays
    Course.ScheduleHours = ScheduleHours
    Course.CourseTeacher = CourseTeacher

    db.session.commit()
    return Course_Schema.jsonify(Course)

# endpoint to delete user
@app.route("/Course/<CourseID>", methods=["DELETE"])
def Course_delete(CourseID):
    Course = Course.query.filter(Course.CourseID == CourseID).first()
    db.session.delete(Course)
    db.session.commit()

    return Course_Schema.jsonify(Course)
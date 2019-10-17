from CollegeAPI import db, app, materias_schema
from Models.Schedule import Schedule
from Controllers.CourseController import Course_detail
from flask import jsonify,request
from sqlalchemy import and_

@app.route("/Schedule", methods = ["POST"])
def add_Schedule():
    StudentID = request.json['StudentID']
    CourseID = request.json['CourseID']

    new_Schedule = Schedule(StudentID,CourseID)

    db.session.add(new_Schedule)
    db.session.commit()

    return jsonify(True)

#Endpoint to show specific Schedules
@app.route("/Schedule/<StudentID>", methods=["GET"] )
def get_Schedule(StudentID):
    all_Schedules = Schedule.query.filter(Schedule.StudentID == StudentID)
    resultSchedules = materias_schema.dump(all_Schedules)
    all_materias = []
    for materia in resultSchedules : 
        all_materias.append(Course_detail(materia['CourseID']))

    result = materias_schema.dump(all_materias)
    return jsonify(result)

@app.route("/Schedule/<StudentID>/<CourseID>", methods=["DELETE"])
def Schedule_delete(StudentID, CourseID):
    Schedules = Schedule.query.filter(and_(Schedule.CourseID == CourseID,Schedule.StudentID == StudentID)).first()
    db.session.delete(Schedules)
    db.session.commit()

    return jsonify(True)
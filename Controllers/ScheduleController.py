from CollegeAPI import db, app, materias_schema
from Models.Schedule import Schedule
from flask import jsonify,request

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
    resultSchedules = Schedules_schema.dump(all_Schedules)
    all_materias = []
    for materia in resultSchedules : 
        all_materias.append(materiaGet(materia['CourseID']))

    result = materias_schema.dump(all_materias)
    return jsonify(result)

@app.route("/Schedule/<StudentID>/<codigo>", methods=["DELETE"])
def Schedule_delete(StudentID, codigo):
    Schedule = Schedule.query.filter(and_(Schedule.CourseID == codigo,Schedule.StudentID == StudentID)).first()
    db.session.delete(Schedule)
    db.session.commit()

    return jsonify(True)
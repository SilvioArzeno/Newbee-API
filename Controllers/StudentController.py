from CollegeAPI import db, app, user_schema,users_schema
from Models.Student import Student
from flask import jsonify,request


@app.route("/student", methods = ["POST"])
def add_student():
    StudentID = request.json['StudentID']
    FirstName = request.json['FirstName']
    LastName = request.json['LastName']
    Password = request.json['Password']
    Email = request.json['Email']
    Active = request.json['Active']

    new_student = Student(StudentID,FirstName,LastName,Password,Email,Active)

    db.session.add(new_student)
    db.session.commit()

    return user_schema.jsonify(new_student)

#Endpoint to show all users
@app.route("/student", methods=["GET"] )
def get_students():
    all_students = Student.query.all()
    result = users_schema.dump(all_students)
    return jsonify(result)

# endpoint to get user detail by StudentID
@app.route("/student/<StudentID>", methods=["GET"])
def user_detail(StudentID):
    student = Student.query.filter(Student.StudentID == StudentID).first()
    return user_schema.jsonify(student)


# endpoint to update user
@app.route("/student/<StudentID>", methods=["PUT"])
def user_update(StudentID):
    student = Student.query.filter(Student.StudentID == StudentID).first()
    StudentID = request.json['StudentID']
    FirstName = request.json['FirstName']
    LastName = request.json['LastName']
    Password = request.json['Password']
    Email = request.json['Email']
    Active = request.json['Active']

    student.StudentID = StudentID
    student.FirstName = FirstName
    student.LastName = LastName
    student.Password = Password
    student.Email = Email
    student.Active = Active

    db.session.commit()
    return user_schema.jsonify(student)


# endpoint to delete user
@app.route("/student/<StudentID>", methods=["DELETE"])
def user_delete(StudentID):
    student = Student.query.filter(Student.StudentID == StudentID).first()
    db.session.delete(student)
    db.session.commit()

    return user_schema.jsonify(student)
from CollegeAPI import db, app, user_schema
from Models.Student import Student
from flask import jsonify,request


@app.route("/student", methods = ["POST"])
def add_student():
    matricula = request.json['matricula']
    nombres = request.json['nombres']
    apellidos = request.json['apellidos']
    password = request.json['password']
    email = request.json['email']
    active = request.json['active']

    new_student = Student(matricula,nombres,apellidos,password,email,active)

    db.session.add(new_student)
    db.session.commit()

    return user_schema.jsonify(new_student)

#Endpoint to show all users
@app.route("/student", methods=["GET"] )
def get_students():
    all_students = Student.query.all()
    result = users_schema.dump(all_students)
    return jsonify(result)

# endpoint to get user detail by matricula
@app.route("/student/<matricula>", methods=["GET"])
def user_detail(matricula):
    student = Student.query.filter(Student.matricula == matricula).first()
    return user_schema.jsonify(student)


# endpoint to update user
@app.route("/student/<matricula>", methods=["PUT"])
def user_update(matricula):
    student = Student.query.filter(Student.matricula == matricula).first()
    matricula = request.json['matricula']
    nombres = request.json['nombres']
    apellidos = request.json['apellidos']
    password = request.json['password']
    email = request.json['email']
    active = request.json['active']

    student.matricula = matricula
    student.nombres = nombres
    student.apellidos = apellidos
    student.password = password
    student.email = email
    student.active = active

    db.session.commit()
    return user_schema.jsonify(student)


# endpoint to delete user
@app.route("/student/<matricula>", methods=["DELETE"])
def user_delete(matricula):
    student = Student.query.filter(Student.matricula == matricula).first()
    db.session.delete(student)
    db.session.commit()

    return user_schema.jsonify(student)
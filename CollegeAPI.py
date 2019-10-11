from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import or_,and_
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['HEROKU_POSTGRESQL_BLACK_URL'] 
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    matricula = db.Column(db.String(7),unique = True)
    nombres = db.Column(db.String(30))
    apellidos = db.Column(db.String(30))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    active = db.Column(db.Boolean,default = False,nullable = False)

    def __init__(self,matricula,nombres,apellidos,password,email,active):
        self.matricula = matricula
        self.nombres = nombres
        self.apellidos = apellidos
        self.password = password
        self.email = email
        self.active = active

class UserSchema(ma.Schema):
    class Meta:
        fields = ('matricula','nombres','apellidos','password','email','active')

class Materia(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    codigo = db.Column(db.String(6))
    seccion = db.Column(db.Integer)
    aula = db.Column(db.String(10))
    horarioDias = db.Column(db.String(30))
    horarioHoras = db.Column(db.String(15))
    profesor = db.Column(db.String(50))

    def __init__(self,nombre,codigo,seccion,aula,horarioDias,horarioHoras,profesor):

        self.nombre = nombre
        self.codigo = codigo
        self.seccion = seccion
        self.aula = aula
        self.horarioDias = horarioDias
        self.horarioHoras = horarioHoras
        self.profesor = profesor

class MateriaSchema(ma.Schema):
    class Meta:
        fields = ('nombre','codigo','seccion','aula','horarioDias','horarioHoras','profesor')

class Horario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    studentID = db.Column(db.String(7))
    materiaID = db.Column(db.String(10))

    def __init__(self,studentID,materiaID):

        self.studentID = studentID
        self.materiaID = materiaID

class HorarioSchema(ma.Schema):
    class Meta:
        fields = ('studentID','materiaID')

class Directorio(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    area = db.Column(db.String(50))
    departamento = db.Column(db.String(50))
    encargado = db.Column(db.String(50))
    telefono = db.Column(db.String(10))
    edificio = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))

    def __init__(self,area,departamento,encargado,telefono,edificio,descripcion):
        self.area = area
        self.departamento = departamento
        self.encargado = encargado
        self.telefono = telefono
        self.edificio = edificio
        self.descripcion = descripcion

class DirectorioSchema(ma.Schema):
    class Meta:
        fields = ('area','departamento','encargado','telefono','edificio','descripcion')

directorio_schema = DirectorioSchema()
directorios_schema = DirectorioSchema(many=True)
horario_schema = HorarioSchema()
horarios_schema = HorarioSchema(many=True)
materia_schema = MateriaSchema()
materias_schema = MateriaSchema(many=True)        
user_schema = UserSchema()
users_schema = UserSchema(many= True)

#HomePage
@app.route("/")
def hello():
    return "Welcome to the Newbee API please read git readme.md file for more instructions"
#Endpoint for new student


#-------------- Students--------------------#

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
#---------------Horarios-------------------#
@app.route("/horario", methods = ["POST"])
def add_horario():
    studentID = request.json['StudentID']
    materiaID = request.json['CourseID']

    new_horario = Horario(studentID,materiaID)

    db.session.add(new_horario)
    db.session.commit()

    return jsonify(True)

#Endpoint to show specific horarios
@app.route("/horario/<matricula>", methods=["GET"] )
def get_horario(matricula):
    all_horarios = Horario.query.filter(Horario.studentID == matricula)
    resultHorarios = horarios_schema.dump(all_horarios)
    all_materias = []
    for materia in resultHorarios : 
        all_materias.append(materiaGet(materia['materiaID']))

    result = materias_schema.dump(all_materias)
    return jsonify(result)

@app.route("/horario/<matricula>/<codigo>", methods=["DELETE"])
def horario_delete(matricula, codigo):
    horario = Horario.query.filter(and_(Horario.materiaID == codigo,Horario.studentID == matricula)).first()
    db.session.delete(horario)
    db.session.commit()

    return jsonify(True)

#-------------- Materias--------------------#
def materiaGet(codigo):
    materia = Materia.query.filter(Materia.codigo == codigo).first()
    return materia
#endpoint for new materia
@app.route("/materia", methods = ["POST"])
def add_materia():
    nombre = request.json['nombre']
    codigo = request.json['codigo']
    seccion = request.json['seccion']
    aula = request.json['aula']
    horarioDias = request.json['horarioDias']
    horarioHoras = request.json['horarioHoras']
    profesor = request.json['profesor']

    new_materia = Materia(nombre,codigo,seccion,aula,horarioDias,horarioHoras,profesor)

    db.session.add(new_materia)
    db.session.commit()

    return materia_schema.jsonify(new_materia)

#Endpoint to show all materias
@app.route("/materia", methods=["GET"] )
def get_materia():
    all_materias = Materia.query.all()
    result = materias_schema.dump(all_materias)
    return jsonify(result)

#Endpoint to show detail of a materia by codigo
@app.route("/materia/<codigo>", methods=["GET"])
def materia_detail(codigo):
    materia = Materia.query.filter(Materia.codigo == codigo).first()
    return materia_schema.jsonify(materia)


# endpoint to update materia
@app.route("/materia/<codigo>", methods=["PUT"])
def materia_update(codigo):
    materia = Materia.query.filter(Materia.codigo == codigo).first()
    nombre = request.json['nombre']
    codigo = request.json['codigo']
    seccion = request.json['seccion']
    aula = request.json['aula']
    horarioDias = request.json['horarioDias']
    horarioHoras = request.json['horarioHoras']
    profesor = request.json['profesor']

    materia.nombre = nombre
    materia.codigo = codigo
    materia.seccion = seccion
    materia.aula = aula
    materia.horarioDias = horarioDias
    materia.horarioHoras = horarioHoras
    materia.profesor = profesor

    db.session.commit()
    return materia_schema.jsonify(materia)

# endpoint to delete user
@app.route("/materia/<codigo>", methods=["DELETE"])
def materia_delete(codigo):
    materia = Materia.query.filter(Materia.codigo == codigo).first()
    db.session.delete(materia)
    db.session.commit()

    return materia_schema.jsonify(materia)

#-------------- Directorios--------------------#   

 #endpoint for new directorio
@app.route("/directorio", methods = ["POST"])
def add_directorio():
    
    area = request.json['area']
    departamento = request.json['departamento']
    encargado = request.json['encargado']
    telefono = request.json['telefono']
    edificio = request.json['edificio']
    descripcion = request.json['descripcion']

    new_directorio = Directorio(area,departamento,encargado,telefono,edificio,descripcion)

    db.session.add(new_directorio)
    db.session.commit()

    return directorio_schema.jsonify(new_directorio)

#Endpoint to show all directorios
@app.route("/directorio", methods=["GET"] )
def get_directorio():
    all_directorios = Directorio.query.all()
    result = directorios_schema.dump(all_directorios)
    return jsonify(result)

#Endpoint to show detail of a directorio by area
@app.route("/directorio/<area>", methods=["GET"])
def directorio_detail_area(area):
    directorio_details = Directorio.query.filter(or_(Directorio.departamento == area,Directorio.area == area))
    result = directorios_schema.dump(directorio_details)

    return jsonify(result)

# endpoint to update directorio
@app.route("/directorio/<departamento>", methods=["PUT"])
def directorio_update(departamento):
    directorio = Directorio.query.filter_by(Directorio.departamento == departamento).first()
    area = request.json['area']
    departamento = request.json['departamento']
    encargado = request.json['encargado']
    telefono = request.json['telefono']
    edificio = request.json['edificio']
    descripcion = request.json['descripcion']

    directorio.area = area
    directorio.departamento = departamento
    directorio.encargado = encargado
    directorio.telefono = telefono
    directorio.edificio = edificio
    directorio.descripcion = descripcion

    db.session.commit()
    return directorio_schema.jsonify(directorio)

# endpoint to delete directorio
@app.route("/directorio/<departamento>", methods=["DELETE"])
def directorio_delete(departamento):
    directorio = Directorio.query.filter(Directorio.departamento == departamento).first()
    db.session.delete(directorio)
    db.session.commit()

    return directorio_schema.jsonify(directorio)



if __name__ == '__main__':
    app.run(debug=True)

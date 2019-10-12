from flask_sqlalchemy import SQLAlchemy
from CollegeAPI import ma
from CollegeAPI import app


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
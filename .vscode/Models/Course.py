from CollegeAPI import ma
from CollegeAPI import db
from CollegeAPI import app

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

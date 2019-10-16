from CollegeAPI import ma,db,app

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    StudentID = db.Column(db.String(7))
    MateriaID = db.Column(db.String(10))

    def __init__(self,StudentID,MateriaID):

        self.StudentID = StudentID
        self.MateriaID = MateriaID

class ScheduleSchema(ma.Schema):
    class Meta:
        fields = ('StudentID','MateriaID')
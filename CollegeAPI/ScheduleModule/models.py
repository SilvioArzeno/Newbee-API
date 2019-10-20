from CollegeAPI import ma,db

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    StudentID = db.Column(db.String(7))
    CourseID = db.Column(db.String(10))

    def __init__(self,StudentID,CourseID):

        self.StudentID = StudentID
        self.CourseID = CourseID

class ScheduleSchema(ma.Schema):
    class Meta:
        fields = ('StudentID','CourseID')
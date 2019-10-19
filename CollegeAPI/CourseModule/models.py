from CollegeAPI import ma,db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    CourseName = db.Column(db.String(50))
    CourseID = db.Column(db.String(6))
    CourseSection = db.Column(db.Integer)
    CourseRoom = db.Column(db.String(10))
    ScheduleDays = db.Column(db.String(30))
    ScheduleHours = db.Column(db.String(15))
    CourseTeacher = db.Column(db.String(50))

    def __init__(self,CourseName,CourseID,CourseSection,CourseRoom,ScheduleDays,ScheduleHours,CourseTeacher):

        self.CourseName = CourseName
        self.CourseID = CourseID
        self.CourseSection = CourseSection
        self.CourseRoom = CourseRoom
        self.ScheduleDays = ScheduleDays
        self.ScheduleHours = ScheduleHours
        self.CourseTeacher = CourseTeacher

class CourseSchema(ma.Schema):
    class Meta:
        fields = ('CourseName','CourseID','CourseSection','CourseRoom','ScheduleDays','ScheduleHours','CourseTeacher')
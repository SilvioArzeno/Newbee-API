from CollegeAPI import ma,db

class Task(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    TaskID = db.Column(db.String(20),unique = True)
    TaskName = db.Column(db.String(50))
    TaskDescription = db.Column(db.String(100))
    TaskDueDate = db.Column(db.DateTime)
    TaskDone = db.Column(db.Boolean, default = False)

    def __init__(self,TaskID,TaskName,TaskDescription,TaskDueDate,TaskDone):
        self.TaskID = TaskID
        self.TaskName = TaskName
        self.TaskDescription = TaskDescription
        self.TaskDueDate = TaskDueDate
        self.TaskDone = TaskDone

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('TaskID','TaskName','TaskDescription','TaskDueDate','TaskDone')
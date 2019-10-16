from CollegeAPI import ma,db,app


class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    StudentID = db.Column(db.String(7),unique = True)
    FirstName = db.Column(db.String(30))
    LastName = db.Column(db.String(30))
    Password = db.Column(db.String(50))
    Email = db.Column(db.String(50))
    Active = db.Column(db.Boolean,default = False,nullable = False)

    def __init__(self,StudentID,FirstName,LastName,Password,Email,Active):
        self.StudentID = StudentID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Password =  Password
        self.Email = Email
        self.Active = Active

class UserSchema(ma.Schema):
      class Meta:
        fields = ('StudentID','FirstName','LastName','Password','Email','Active')
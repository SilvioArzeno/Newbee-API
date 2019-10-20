from CollegeAPI import ma,db

class Directory(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    Area = db.Column(db.String(50))
    Department = db.Column(db.String(50))
    Supervisor = db.Column(db.String(50))
    PhoneNumber = db.Column(db.String(10))
    Location = db.Column(db.String(50))
    Description = db.Column(db.String(100))

    def __init__(self,Area,Department,Supervisor,PhoneNumber,Location,Description):
        self.Area = Area
        self.Department = Department
        self.Supervisor = Supervisor
        self.PhoneNumber = PhoneNumber
        self.Location = Location
        self.Description = Description

class DirectorySchema(ma.Schema):
    class Meta:
        fields = ('Area','Department','Supervisor','PhoneNumber','Location','Description')
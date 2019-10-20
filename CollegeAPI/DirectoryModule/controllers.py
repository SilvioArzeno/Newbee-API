from CollegeAPI import db, app
from models import Directory,DirectorySchema
from flask import jsonify,request,Blueprint

app = Blueprint('DirectoryModule',__name__)
Directory_Schema = DirectorySchema()
Directories_Schema = DirectorySchema(many=True)
#endpoint for new Directory
@app.route("/Directory", methods = ["POST"])
def add_Directory():
    
    Area = request.json['Area']
    Department = request.json['Department']
    Supervisor = request.json['Supervisor']
    PhoneNumber = request.json['PhoneNumber']
    Location = request.json['Location']
    Description = request.json['Description']

    new_Directory = Directory(Area,Department,Supervisor,PhoneNumber,Location,Description)

    db.session.add(new_Directory)
    db.session.commit()

    return Directory_Schema.jsonify(new_Directory)

#Endpoint to show all Directorys
@app.route("/Directory", methods=["GET"] )
def get_Directory():
    all_Directorys = Directory.query.all()
    result = Directories_Schema.dump(all_Directorys)
    return jsonify(result)

#Endpoint to show detail of a Directory by Area
@app.route("/Directory/<Area>", methods=["GET"])
def Directory_detail_Area(Area):
    Directory_details = Directory.query.filter(or_(Directory.Department == Area,Directory.Area == Area))
    result = Directories_Schema.dump(Directory_details)

    return jsonify(result)

# endpoint to update Directory
@app.route("/Directory/<Department>", methods=["PUT"])
def Directory_update(Department):
    Directory = Directory.query.filter_by(Directory.Department == Department).first()
    Area = request.json['Area']
    Department = request.json['Department']
    Supervisor = request.json['Supervisor']
    PhoneNumber = request.json['PhoneNumber']
    Location = request.json['Location']
    Description = request.json['Description']

    Directory.Area = Area
    Directory.Department = Department
    Directory.Supervisor = Supervisor
    Directory.PhoneNumber = PhoneNumber
    Directory.Location = Location
    Directory.Description = Description

    db.session.commit()
    return Directory_Schema.jsonify(Directory)

# endpoint to delete Directory
@app.route("/Directory/<Department>", methods=["DELETE"])
def Directory_delete(Department):
    Directory = Directory.query.filter(Directory.Department == Department).first()
    db.session.delete(Directory)
    db.session.commit()

    return Directory_Schema.jsonify(Directory)

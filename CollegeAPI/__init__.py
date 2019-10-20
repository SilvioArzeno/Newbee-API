from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)
ma = Marshmallow(app)

#Blueprints registration
from CollegeAPI.StudentModule.controllers import app as StudentModule
from CollegeAPI.CourseModule.controllers import app as CourseModule
from CollegeAPI.DirectoryModule.controllers import app as DirectoryModule
from CollegeAPI.ScheduleModule.controllers import app as ScheduleModule

app.register_blueprint(StudentModule)
app.register_blueprint(CourseModule)
app.register_blueprint(DirectoryModule)
app.register_blueprint(ScheduleModule)


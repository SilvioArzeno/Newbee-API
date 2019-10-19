from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from CollegeAPI.StudentModule.controllers import app as StudentModule
app.register_blueprint(StudentModule)


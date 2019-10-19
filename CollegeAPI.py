'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import or_,and_
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__)) #This can be eliminated in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'NewBeeCore.sqlite') #os.environ['HEROKU_POSTGRESQL_BLACK_URL'] #Production DB
db = SQLAlchemy(app)
ma = Marshmallow(app)
from Controllers.StudentController import StudentEndpoint
app.register_blueprint(StudentEndpoint)



if __name__ == '__main__':
    app.run(debug=True)
'''
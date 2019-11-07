import os


basedir = os.path.abspath(os.path.dirname(__file__)) #This can be eliminated in production
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_DATABASE_URI = os.environ['HEROKU_POSTGRESQL_BLACK_URL'] 
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'NewBeeCore.sqlite')

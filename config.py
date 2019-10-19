import os


basedir = os.path.abspath(os.path.dirname(__file__)) #This can be eliminated in production
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'NewBeeCore.sqlite') #os.environ['HEROKU_POSTGRESQL_BLACK_URL'] #Production DB

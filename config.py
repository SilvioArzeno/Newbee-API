import os

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ['HEROKU_POSTGRESQL_BLACK_URL'] #Production DB

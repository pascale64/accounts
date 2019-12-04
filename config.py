import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'any_thing_you_like'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://accounting:password@localhost/bdf'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

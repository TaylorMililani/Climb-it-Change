import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = 'postgres://viufcoiovftbmz:0cb59911680aab744f8b6597f7b8b9559696946dad4b9ec4d14cf18e336215e1@ec2-3-211-245-154.compute-1.amazonaws.com:5432/dcfqr78dkeju71'
    # os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False 


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
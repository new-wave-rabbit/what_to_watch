import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    JSON_AS_ASCII = False
    JSON_PROVIDER_CLASS = None
    DROPBOX_TOKEN = os.getenv('DROPBOX_TOKEN') 


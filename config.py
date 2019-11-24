import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))

#class Config(object):
DEBUG = False
TESTING = False
SECRET_KEY = 'this-really-needs-to-be-changed'
MONGODB_HOST = 'mongodb+srv://<user1>:<pwd1>@cluster.mongodb.net/test?retryWrites=true&w=majority'


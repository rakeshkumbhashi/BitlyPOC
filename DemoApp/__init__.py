from flask import Flask
from flask_mongoengine import MongoEngine
from mongoengine import connect

#connect('test', "mongodb+srv://user:user123@cluster0-dzjug.mongodb.net/test?retryWrites=true&w=majority")
db = MongoEngine()


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.app_context().push()
    
    from .app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    db.init_app(app)
    return app
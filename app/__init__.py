from flask import Flask
from config import config_options

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# Initializing app
def create_app(config_name):
    app = Flask(__name__)


    # Setting up configurations
    app.config.from_object(DevConfig)
    app.config.from_pyfile('config.py')

    # bootstrap = Bootstrap()
    # db = SQLAlchemy()

    bootstrap.init_app(app)
    db.init_app(app)


    from app import views

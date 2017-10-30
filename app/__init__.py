from flask import Flask
from .config import DevConfig


# Initializing app
app = Flask(__name__)


# Setting up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views

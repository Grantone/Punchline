from flask import Flask


# Initializing app
app = Flask(__name__)


# Setting up configurations
app.config.from_object(DevConfig)


from app import views

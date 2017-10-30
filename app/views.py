from flask import render_template
from app import app

# views
@app.route('/')
def index():

    message = 'One Minute Pitch'
    return render_template('index.html',message = message)

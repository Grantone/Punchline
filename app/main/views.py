from flask import render_template
from app import app

# views
@app.route('/category/<int:category_id>')
def index():

    message = 'One Minute Pitch'
    return render_template('category.html',id = category_id)

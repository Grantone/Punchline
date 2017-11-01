from flask import render_template
from . import auth
from ..models import User
from .. import db


@auth.route('/login')
def login():
    return render_template('auth/login.html')

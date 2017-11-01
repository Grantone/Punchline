from . import db
from datetime import datetime
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True)
    name = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    comments = db.relationship('Comment', backref='user', lazy="dynamic")
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

        def verify_password(self, password):
            return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.name}'


class Comment(db.Model):

    all_comments = []

    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)

    def save_comment(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls, id):

        response = []

        for comment in cls.all_comments:
            if comment.category_id == id:
                response.append(comment)

            return response


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer)
    category_title = db.Column(db.String)
    category_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

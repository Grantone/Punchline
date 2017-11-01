from . import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'categories'
id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    db.Column(db.Integer,db.ForeignKey('roles.id'))

    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    def __repr__(self):
        return f'User {self.name}'

class Comment(db.Model):

    all_comments = []

    __tablename__ = 'comments'
    id =db.Column(db.Integer,primary_key = True)

    def save_comment(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id =db.Column(db.Integer,primary_key = True)
    category_id = db.Column(db.Integer)
    category_title = db.Column(db.String)
    category_date = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

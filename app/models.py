from . import db
from datetime import datetime
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):

        categories = Category.query.all()
        return categories

    def __repr__(self):
        return f'User {self.name}'


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    comments = db.relationship('Comment', backref='user', lazy="dynamic")
    pitches = db.relationship("Pitch", backref="user", lazy="dynamic")pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

        def verify_password(self, password):
            return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


class Comment(db.Model):

    all_comments = []

    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_section_id = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches_id"))

    def save_comment(self):
        db.session.add(self)
        db.session.comment()

    @classmethod
    def get_comments(self, id):
        comments = Comment.query.filter_by(pitches_id=id).all()
        return comments


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    categoty_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    comment = db.relationship("Comments", backref="pitch", lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(category_id=id).all()
        return pitches

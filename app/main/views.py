from flask import render_template, redirect, url_for, abort
from . import main
from ..models import Pitch, Category, Comment
from flask_login import login_required, current_user
from .forms import CommentForm, PitchForm
from datetime import datetime


@main.route('/')
def index():

    category = Category.get_categories(id)
    pitch = Pitch.get_all_pitches()
    title = 'Home - Welcome to PunchLine'
    return render_template('index.html', title=title, category=category, pitch=pitch)


@main.route('/category/<int:id>')
def category(id):
    category = Category.query.get(id)
    # pitches = Pitch.get_all_pitches(id)
    form = PitchForm()
    title = 'pitches'

    return render_template('category.html', category=category, title=title, pitch_form=form)

    # pitch=pitch,


@main.route('/category/pitch/new/<int:id>', methods=["GET", "POST"])
@login_required
def new_pitch(id):
    category = Category.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    form = PitchForm()

    if form.validate_on_submit():
        content = form.content.data
        new_pitch = Pitch(
            name=name, category_id=category.id, user_id=current_user.id)

        new_pitch.save_pitch()

        return redirect(url_for('.category', id=category.id))

    title = "New Pitch"
    return render_template('category.html', pitch_form=form, title=title)


@main.route('/pitch/<int:id>')
def single_pitch(id):
    pitch = Pitch.query.get(id)
    comment = Comments.get_comment(pitch.id)

    title = "Pitch page"

    return render_template('pitch.html', pitch=pitch, comment=comment, title=title)


@main.route('/pitch/new/<int:id>', methods=["GET", "POST"])
@login_required
def new_comment(id):
    pitch = Pitch.query.filter_by(id=id).first()
    if pitch is None:
        abort(404)

    form = CommentForm()

    if form.validate_on_submit():
        body = form.body.data
        new_comment = Comments(
            body=body, pitch_id=pitch.id, user_id=current_user.id)

        new_comment.save_comment()

        return redirect(url_for('.single_pitch', id=pitch.id))

    title = "New Comment"
    return render_template('new_comment.html', comment_form=form, title=title)

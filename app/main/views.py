from flask import render_template
from ..models import Comment, Category
from .forms import CommentForm
# from app import app
from . import main
from flask_login import login_required


# views
@main.route('/')
def index():

    title = 'Home - Welcome to One Minute Pitch web'
    return render_template('index.html', title=title)


@main.route('/category/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    category = get_category(id)

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        new_comment = Comment(category.id, title, comment)
        new_comment.save_comment()
        return redirect(url_for('category', id=category.id))

    # title = f'{category.name} comment'
    return render_template('new_comment.html', title=title, comment_form=form, category=category)


@main.route('/category/<int:id>')
def category(id):

    category = Category.get_categories(id)
    # title = f'{category.name}'
    comments = Comment.get_comments(category.id)

    return render_template('category.html', title=title, category=category, comments=comments)

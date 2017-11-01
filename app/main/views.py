from flask import render_template
from ..models import Comment
from .forms import CommentForm
# from app import app
from . import main
from flask_login import login_required


# views
@main.route('/')
def index():

    #
    # #categories
    # pickup_lines = get_categories('pickupLine')
    # interview_pitch = get_categories('interviewPitch')
    # product_pitch = get_categories('productPitch')
    # promotion_pitch = get_categories('promotionPitch')
    #
    # ,title = title, punchLine = punchLine_categories, interviewPitch = interviewPitch_categories, productPitch = productPitch_categories, promotionPitch = promotionPitch_categories

    title = 'Home - Welcome to One Minute Pitch web'
    return render_template('index.html', title=title)

    # message = 'One Minute Pitch'
    # return render_template('category.html',id = category_id)


@main.route('/category/comment/new/<int:id>', methods=['GET', 'POST'])
def new_comment(id):
    form = CommentForm()
    category = get_category(id)

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        new_comment = Comment(category.id, title, comment)
        new_comment.save_comment()
        return redirect(url_for('category', id=category.id))

    title = f'{category.title} comment'
    return render_template('new_comment.html', title=title, comment_form=form, category=category)


@main.route('/category/<int:id>')
def category(id):

    category = get_category(id)
    title = f'{category.title}'
    comments = Comment.get_comments(category_id)

    return render_template('category.html', title=title, category=category, comments=comments)

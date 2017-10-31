from flask import render_template
from app import app

# views
@app.route('/category/<int:category_id>')
def index():



    #categories
    pickup_lines = get_categories('pickupLine')
    interview_pitch = get_categories('interviewPitch')
    product_pitch = get_categories('productPitch')
    promotion_pitch = get_categories('promotionPitch')




    title = 'Home - Welcome to One Minute Pitch web'
    return render_template('index.html',title = title, punchLine = punchLine_categories, interviewPitch = interviewPitch_categories, productPitch = productPitch_categories, promotionPitch = promotionPitch_categories)


    # message = 'One Minute Pitch'
    # return render_template('category.html',id = category_id)

import re
from flask import render_template, session, redirect, request
from idefy_app import app
from idefy_app.models.user import User
from idefy_app.models.category import Category
from idefy_app.models.idea import Idea
from flask_bcrypt import Bcrypt
from flask import flash

# ==================================================Display pages===========================================

@app.route('/category', methods = ['GET'])
def displayCategoryform():
    
    categoryes = Category.getcategories()

    return render_template('addcategory.html', categories = categoryes)

    


# ==================================================Add and validate categories===========================================

@app.route('/add/category', methods = ['POST'])
def addCat():

    categoryinfo = {
    'category' : request.form['category']
    }

    if Category.categoryValidations(categoryinfo):
        Category.addcategory(categoryinfo)
        return redirect ('/dashboard')
    else:
        return redirect('/category')
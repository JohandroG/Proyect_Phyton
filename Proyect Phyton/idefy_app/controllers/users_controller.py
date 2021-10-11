import re
from flask import render_template, session, redirect, request
from idefy_app import app
from idefy_app.models.user import User
from flask_bcrypt import Bcrypt
from flask import flash

# ==================================================Display pages===========================================

@app.route('/register', methods = ['GET'])
def displayRegisterinfo():
    
    return render_template('register.html')

@app.route('/login', methods = ['GET'])
def displayLogininfo():
    
    return render_template('login.html')
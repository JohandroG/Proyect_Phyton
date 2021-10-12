import re
from flask import render_template, session, redirect, request
from idefy_app import app
from idefy_app.models.user import User
from idefy_app.models.category import Category

from flask_bcrypt import Bcrypt
from flask import flash
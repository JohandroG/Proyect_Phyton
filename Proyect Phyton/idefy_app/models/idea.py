from idefy_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re

class Idea:
    def __init__(self,data):
        
        self.idea_id = data['idea_id']
        self.idea_info = data['idea_info']
        self.likes = data['likes']
        self.category = data['category']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


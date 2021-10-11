from idefy_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re


class User:
    def __init__(self,data):
        
        self.first_name = data['first_name']
        self.first_name = data['last_name']
        self.first_name = data['username']
        self.first_name = data['email']
        self.first_name = data['password']

#==========================================================================================================

    @classmethod
    def registerUser(cls,data):
        query = "INSERT INTO users (first_name,last_name,username,email,user_password,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(username)s,%(email)s,%(encryptedpassword)s,SYSDATE(),SYSDATE())"
        results = connectToMySQL('idefy').query_db(query,data)
        return results

#==========================================================================================================

    @classmethod
    def validatelogin1(cls,loginInfo):
        query = "SELECT * FROM users WHERE email = %(email)s"
        email = {
                "email" : loginInfo,
            }
        results = connectToMySQL('idefy').query_db(query,email)
        return results

    @classmethod
    def validatelogin2(cls,loginInfo):
        query = "SELECT * FROM users WHERE username = %(username)s"
        username = {
                "username" : loginInfo,
            }
        results = connectToMySQL('idefy').query_db(query,username)
        return results

    @classmethod
    def validatelogin3(cls,loginInfo):
        query = "SELECT * FROM users WHERE user_id = %(id)s"
        id = {
                "id" : loginInfo,
            }
        results = connectToMySQL('idefy').query_db(query,id)
        return results

#==========================================================================================================

    @staticmethod
    def registerValidations(data):

        isValid = True

        if len(data['first_name']) < 3:
            flash("The first Name must be at least 3 characters")
            isValid = False
        if len(data['last_name']) < 3:
            flash("The Last Name must be at least 3 characters")
            isValid = False
        if len(data['password']) < 8:
            flash("The Password must be at least 8 characters")
            isValid = False
        if len(data['password']) != len(data['conpass']):
            flash("The Passwords do not match")
            isValid = False
        return isValid


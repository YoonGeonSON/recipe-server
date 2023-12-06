from flask import request
from flask import request
from flask_restful import Resource
from mysql_connention import get_connection
from mysql.connector import Error

class UserRegisterResource(Resource) :

    def post(self) :
        return















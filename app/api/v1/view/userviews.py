from flask import request
from flask_restful import Resource, reqparse
from app.api.v1.model.models import UserModels

parser = reqparse.RequestParser()
parser.add_argument(
    "firstname", type= str, required = True, help= "First name field is required")
parser.add_argument(
    "lastname", type= str, required = True, help= "Last name field is required")
parser.add_argument(
    "othernames", type=str, required = True, help = "Other name field is required")
parser.add_argument(
    "email", type= str, required = True, help= "Email field is required"
    )
parser.add_argument(
    "password", type= str, required = True, help = "Password field is required"
)
parser.add_argument(
    "phoneNumber", type= str, required = True, help = "Phone number field is required")
parser.add_argument(
    "username", type= str, required = True, help = "Username is required")
parser.add_argument(
    "registered", type= str, required = False)



class GetError():
    def notFound(self):
        return {'Message' : 'Record not found','status':404},404


class User(Resource, GetError): 
    #This class and its members creates an endpoint that acts on one specific User at a time 
    def __init__(self):
        self.db = UserModels()

    def notFound(self):
        return {'Message' : 'Record not found'},404

    def get(self, user_id):
        user = self.db.find(user_id)

        if not user:
            return self.notFound()

        return {
            'Message' : 'The specific user has been returned successfully',
            'data' : user
            }, 200 

    def patch(self, user_id):
        data = parser.parse_args()
        user = self.db.find(user_id)
        if user:
            user.update(data)
            return {'Message' : 'Successfully updated',
                    'data' : user
                    }, 200
        else:
            return self.notFound()


class UserbyUsername(Resource, GetError):
    #This class and its functions creates an endpoint that allows login in of users

    def __init__(self):
        self.db = UserModels()

    def get(self, user_name):
        user = self.db.find_by_username(user_name)

        if not user:
            return self.notFound()
    
        return{
            'Message' : 'The specific user has been found',
            'data' : user
        }, 200 

    def patch(self, user_name):
        data = parser.parse_args()
        user = self.db.find_by_username(user_name)
        if user:
            user.update(data)
            return {'Message' : 'Successfully updated',
                    'data' : user
                    }, 200
        else:
            return self.notFound()
    
            
        
    
    def post(self, username): 
        #login in an existing user
        
        data = parser.parse_args()
        user = self.db.find_by_username(data['username'])

        if user:
            if user['password'] == data['password']:
                return {
                    'Message' : 'User successfully logged in',
                }, 200
            else:
                return {
                    'Message' : 'Invalid password'
                }, 422
        else:
            return {
                'Message' : 'User not found'
            }, 404

class Users(Resource, GetError):
    #This class and its members creates an endpoint that acts on many Users at a time

    def __init__(self):
        self.db = UserModels()

    def get(self):
        return{
            'Message': 'Users returned successfully',
            'data': self.db.all()
            }, 200 

    def post(self):
        #register a new user
        
        data = parser.parse_args()

        user = {
            'firstname' : data['firstname'],
            'lastname' : data['lastname'],
            'othernames' : data['othernames'],
            'email' : data['email'],
            'password' : data['password'],
            'phoneNumber' : data['phoneNumber'],
            'username' : data['username'], 
            'registered' : data['registered'],
            }
        
        if data['firstname'] == "" or data['firstname'] == " ":
            return "Firstname required!"
        elif data['lastname'] == "" or data['lastname']== " ": 
            return "lastname required!"
        elif data['othernames'] == "" or data['othernames']== " ":
            return "othernames required!"
        elif data['email'] == "" or data['email']== " ":
            return "email required!"
        elif data['password'] == "" or data['password']== " ":
            return "password required!"
        elif data['username'] == "" or data['username']== " ":
            return "Username required!"
        else:
                
            self.db.save(user)
            return {
                'Message' : 'User saved successfully',
                'data' : user
                }, 201
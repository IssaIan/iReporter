from flask import request
from flask_restful import Api, Resource
from app.api.v1.model.models import UserModels


class User(Resource):

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
        data = request.get_json()
        user = self.db.find(user_id)
        if user:
            user.update(data)
            return {'Message' : 'Successfully updated',
                    'data' : user
                    }, 200
        else:
            return self.notFound()

class Users(Resource):

    def __init__(self):
        self.db = UserModels()

    def notFound(self):
        return {'Message' : 'Record not found'},404

    def get(self):
        return{
            'Message': 'Users returned successfully',
            'data': self.db.all()
            }, 200 

    def post(self):
        data = request.get_json()

        user = {
            'firstname' : data['firstname'],
            'lastname' : data['lastname'],
            'othernames' : data['othernames'],
            'email' : data['email'],
            'phoneNumber' : data['phoneNumber'],
            'username' : data['username'], 
            'registered' : data['registered'],
            }
        
        self.db.save(user)
        return {
            'Message' : 'User saved successfully',
            'data' : user
            }, 201
from flask import Flask
from flask_restful import Api, Resource
from app.api.v1.view.views import Incident, Incidents
from app.api.v1.view.userviews import User, Users
from .api.v1 import version_one as v1

def create_app():
    app = Flask(__name__)
    api = Api(v1)
    api.add_resource(Incident, '/incidents/<int:incident_id>') #for a specific incident
    api.add_resource(Incidents, '/incidents')  #for the list of incidents
    api.add_resource(User, '/users/<int:user_id>')#for an individual user
    api.add_resource(Users, '/users')#list of all users
    app.register_blueprint(v1)
    return app 
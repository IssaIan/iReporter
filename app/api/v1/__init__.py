from flask_restful import Api, Resource
from flask import Blueprint
from app.api.v1.view.views import Incident, Incidents
from app.api.v1.view.userviews import User, Users


version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(version_one)
api.add_resource(Incident, '/incidents/<int:incident_id>') #for a specific incident
api.add_resource(Incidents, '/incidents')  #for the list of incidents
api.add_resource(User, '/users/<int:user_id>')#for an individual user
api.add_resource(Users, '/users')#list of all users

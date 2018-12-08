from flask_restful import Api, Resource
from flask import Blueprint
from app.api.v1.view.views import Incident, Incidents, Location, Description
from app.api.v1.view.userviews import User, Users, UserbyUsername

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(version_one)
# for a specific incident
api.add_resource(Incident, '/incidents/<int:incident_id>')
api.add_resource(Incidents, '/incidents')  # for the list of incidents
api.add_resource(User, '/users/<int:user_id>')  # for an individual user
api.add_resource(Users, '/users')  # list of all users
# updating location
api.add_resource(Location, '/incidents/<int:incident_id>/location')
# updating description
api.add_resource(Description, '/incidents/<int:incident_id>/description')
# gets a user by their username and also enables patching
api.add_resource(UserbyUsername, '/users/<user_name>')

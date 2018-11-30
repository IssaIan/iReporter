from flask import Flask, Blueprint
from flask_restful import Api, Resource

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1/')
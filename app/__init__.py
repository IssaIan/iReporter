from flask import Flask, Blueprint
#from instance.config import app_config
# from db_config import create_tables

from .api.v1 import version_one as v1

def create_app(config_name):
    app = Flask(__name__)
    app.register_blueprint(v1)
    return app


# def create_app():#config_name='development'):
#     app = Flask(__name__)#(__name__, instance_relative_config=True)
#     #app.url_map.strict_slashes = False
#     #app.config.from_object(app_config[config_name])
#     #app.config.from_pyfile('config.py')
#     # create_tables()
#     app.register_blueprint(v1)
#     return app
  

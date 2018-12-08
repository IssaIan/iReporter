from flask import Flask, Blueprint, jsonify, request
from instance.config import app_config

from .api.v1 import version_one as v1


def create_app(config_name='testing'):
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config['testing'])
    app.config.from_pyfile('config.py')
    app.register_blueprint(v1)

    @app.errorhandler(404)
    def invalid_endpoint(error=None):
        """Handle wrong endpoints."""
        return jsonify({
            'message': '{} is not a valid url'.format(request.url)
        }), 404

    @app.errorhandler(405)
    def wrong_request_method(error=None):
        """Handle wrong methods for endpoints."""
        request_method = request.method
        return jsonify({
            'message': 'The {} method is not allowed for this endpoint'
            .format(request_method)}), 405

    return app

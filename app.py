import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config:
        # load the test config
        app.config.from_mapping(test_config)

    @app.route('/')
    def index_page():
        return 'Hello, World!'

    return app

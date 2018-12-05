import logging
from flask import current_app, Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Setup the data model.
    db.init_app(app)

    # Register the Bookshelf CRUD blueprint.
    from checkapp.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # Add a default root route.
    @app.route("/")
    def index():
        return "hola"

    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    return app


from checkapp import models

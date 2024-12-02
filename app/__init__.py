from flask import Flask, jsonify
from flask_smorest import Api

from app.blueprint.authentication_blueprint import auth_blp
from app.blueprint.user_blueprint import user_blp
from app.blueprint.job_posting_blueprint import job_posting_blp
from app.blueprint.job_performance_blueprint import job_performance_blp
from app.blueprint.job_interaction_blueprint import job_interaction_blp
from app.blueprint.application_blueprint import application_blp
from app.blueprint.message_blueprint import message_blp

from app.extension import db, migrate
from config import Config
from app.models import authentication_model
from app.models import user_model
from app.models import job_posting_model
from app.models import job_interaction_model
from app.models import job_performance_model
from app.models import application_model
from app.models import message_model

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Set up API
    api = Api(app)
    api.register_blueprint(auth_blp)
    api.register_blueprint(user_blp)
    api.register_blueprint(job_posting_blp)
    api.register_blueprint(job_performance_blp)
    api.register_blueprint(job_interaction_blp)
    api.register_blueprint(application_blp)
    api.register_blueprint(message_blp)


    # Create the database tables automatically
    with app.app_context():
        db.create_all()  # This will create all tables defined in models

    # Default route
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Job Platform API"})

    return app

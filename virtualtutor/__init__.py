"""
Virtual Tutor - An adaptive learning platform using Bayesian Knowledge Tracing
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Application factory pattern for creating Flask app instance"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from virtualtutor import routes
    app.register_blueprint(routes.bp)

    with app.app_context():
        db.create_all()

    return app

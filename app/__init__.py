from flask import Flask, render_template
from flask_migrate import Migrate
from .database import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///model.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    from app.api import main
    app.register_blueprint(main)

    return app
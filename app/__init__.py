from flask import Flask
from .extension import db, migrate
from .config import config
import os

def create_app():
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[env])

    db.init_app(app)
    migrate.init_app(app, db)

    from .api import users_bp
    app.register_blueprint(users_bp)

    return app 

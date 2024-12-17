from flask import Flask
from database.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)

    from app.routes import routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app

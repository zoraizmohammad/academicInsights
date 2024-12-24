from flask import Flask
from flask_cors import CORS
from firebase_admin import credentials, initialize_app

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    CORS(app)

    # Initialize Firebase
    cred = credentials.Certificate(app.config["FIREBASE_ADMIN_KEY"])
    initialize_app(cred)

    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

    return app

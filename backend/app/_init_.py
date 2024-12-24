from flask import Flask
from flask_cors import CORS
from firebase_admin import credentials, initialize_app

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    CORS(app)

    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    app.logger = logging.getLogger()

    # Initialize Firebase
    cred = credentials.Certificate(app.config["FIREBASE_ADMIN_KEY"])
    initialize_app(cred)

        # Add Prometheus metrics
    metrics = PrometheusMetrics(app)
    metrics.info("app_info", "Application info", version="1.0.0")

    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

    return app

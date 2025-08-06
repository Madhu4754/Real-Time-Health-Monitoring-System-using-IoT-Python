from flask import Flask
from .routes import main
from .database import init_db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.register_blueprint(main)
    init_db(app)
    return app

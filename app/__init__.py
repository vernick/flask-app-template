from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes and register them
    from app.routes import main
    app.register_blueprint(main)

    return app

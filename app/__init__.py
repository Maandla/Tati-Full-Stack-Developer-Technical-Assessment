from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import meter_bp
    app.register_blueprint(meter_bp, url_prefix='/meter')
    
    return app

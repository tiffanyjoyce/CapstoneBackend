from flask import Flask

from config import Config

from .api.routes import api

from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources = {r"/*": {"origins": "*"}})

app.register_blueprint(api)

from . import routes
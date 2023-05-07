from flask import Flask

from config import Config

from .api.routes import api

from flask_cors import CORS
from flask_migrate import Migrate
from .models import db

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources = {r"/*": {"origins": "*"}})

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(api)

from . import routes
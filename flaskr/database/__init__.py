import logging
from logging import config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = 'my secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@0.0.0.0:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow(app)

manager = LoginManager(app)

config.fileConfig(fname='logs/logger.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

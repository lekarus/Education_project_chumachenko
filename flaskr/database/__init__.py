from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@0.0.0.0:5432/postgres'


db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow(app)

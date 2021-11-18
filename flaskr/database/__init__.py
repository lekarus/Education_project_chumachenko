from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@0.0.0.0:5432/postgres'


db = SQLAlchemy()
db.init_app(app)

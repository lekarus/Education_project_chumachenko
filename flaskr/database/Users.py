from . import db


class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)
    films = db.relationship("Films", back_populates='user')

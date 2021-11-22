from flask_login import UserMixin

from . import db, ma, manager


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)
    films = db.relationship("Films", back_populates='user')

    def __init__(self, username, password, is_admin):
        self.username = username
        self.password = password
        self.isAdmin = is_admin

    def get_id(self):
        return self.user_id


class UsersSchema(ma.Schema):
    class Meta:
        fields = ['username']


@manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


users_schema = UsersSchema(many=True)

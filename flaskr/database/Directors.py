from . import db


class Directors(db.Model):
    __tablename__ = 'directors'
    __table_args__ = {'extend_existing': True}
    director_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    films_directors = db.relationship("Films_Directors", back_populates='directors')

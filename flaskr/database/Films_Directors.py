from . import db


class Films_Directors(db.Model):
    __tablename__ = 'films_directors'
    __table_args__ = {'extend_existing': True}
    film_id = db.Column(db.Integer, db.ForeignKey('films.film_id'), primary_key=True, nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.director_id'), primary_key=True, nullable=False)
    films = db.relationship("Films", back_populates='films_directors')
    directors = db.relationship("Directors", back_populates='films_directors')


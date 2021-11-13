from . import db


class Films_Genres(db.Model):
    __tablename__ = 'films_genres'
    __table_args__ = {'extend_existing': True}
    film_id = db.Column(db.Integer, db.ForeignKey('films.film_id'), primary_key=True, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), primary_key=True, nullable=False)
    films = db.relationship("Films", back_populates='films_genres')
    genres = db.relationship("Genres", back_populates='films_genres')

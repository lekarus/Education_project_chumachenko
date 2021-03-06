from . import db, ma


class Films(db.Model):
    __tablename__ = 'films'
    __table_args__ = {'extend_existing': True}
    film_id = db.Column(db.Integer, primary_key=True, nullable=False)
    film_title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    film_desc = db.Column(db.Text)
    rating = db .Column(db.Float, nullable=False)
    poster = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    user = db.relationship("Users", back_populates='films')
    films_genres = db.relationship("FilmsGenres", back_populates='films')
    films_directors = db.relationship("FilmsDirectors", back_populates='films')


class FilmsSchema(ma.Schema):
    class Meta:
        fields = ['film_title', 'release_date', 'film_desc', 'poster', 'rating']


films_schema = FilmsSchema(many=True)

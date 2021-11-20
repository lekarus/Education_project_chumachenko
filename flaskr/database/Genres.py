from . import db, ma


class Genres(db.Model):
    __tablename__ = 'genres'
    __table_args__ = {'extend_existing': True}
    genre_id = db.Column(db.Integer, primary_key=True, nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    films_genres = db.relationship("FilmsGenres", back_populates='genres')


class GenresSchema(ma.Schema):
    class Meta:
        fields = ['genre']


genres_schema = GenresSchema(many=True)

from base import *


class Films_Genres(Base):
    __tablename__ = 'films_genres'
    film_id = Column(Integer, ForeignKey('films.film_id'), primary_key=True, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.genre_id'), primary_key=True, nullable=False)
    films = relationship("Films", back_populates='films_genres')
    genres = relationship("Genres", back_populates='films_genres')

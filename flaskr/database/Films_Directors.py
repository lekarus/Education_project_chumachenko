from base import *


class Films_Directors(Base):
    __tablename__ = 'films_directors'
    film_id = Column(Integer, ForeignKey('films.film_id'), primary_key=True, nullable=False)
    director_id = Column(Integer, ForeignKey('directors.director_id'), primary_key=True, nullable=False)
    films = relationship("Films", back_populates='films_directors')
    directors = relationship("Directors", back_populates='films_directors')


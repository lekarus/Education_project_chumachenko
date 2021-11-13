from base import *


class Genres(Base):
    __tablename__ = 'genres'
    genre_id = Column(Integer, primary_key=True, nullable=False)
    genre = Column(String(255), nullable=False)
    films_genres = relationship("Films_Genres", back_populates='genres')

from base import *


class Films(Base):
    __tablename__ = 'films'
    film_id = Column(Integer, primary_key=True, nullable=False)
    film_title = Column(String(255), nullable=False)
    release_date = Column(Date, nullable=False)
    film_desc = Column(String(255))
    poster = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user.id'), nullable=False)
    user = relationship("Users", back_populates='films')
    films_genres = relationship("Films_Genres", back_populates='films')
    films_directors = relationship("Films_Directors", back_populates='films')

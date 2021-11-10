from base import *


class Directors(Base):
    __tablename__ = 'directors'
    director_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    films_directors = relationship("Films_Directors", back_populates='directors')

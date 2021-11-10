from base import *


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(32), nullable=False)
    films = relationship("Films", back_populates='user')

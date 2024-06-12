from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    players = relationship('Player', backref='team')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Team(name={self.name})'

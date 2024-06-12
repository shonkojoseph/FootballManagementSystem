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


@classmethod
def create(cls, name):
    team = cls(name=name)
    session.add(team)
    session.commit()
    return team

@classmethod
def delete(cls, team_id):
    team = session.query(cls).get(team_id)
    if team:
        session.delete(team)
        session.commit()

@classmethod
def get_all(cls):
    return session.query(cls).all()

@classmethod
def find_by_id(cls, team_id):
    return session.query(cls).get(team_id)

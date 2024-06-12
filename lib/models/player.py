from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'))

    def __init__(self, name, team_id):
        self.name = name
        self.team_id = team_id

    def __repr__(self):
        return f'Player(name={self.name}, team_id={self.team_id})'


@classmethod
def create(cls, name, team_id):
    player = cls(name=name, team_id=team_id)
    session.add(player)
    session.commit()
    return player

@classmethod
def delete(cls, player_id):
    player = session.query(cls).get(player_id)
    if player:
        session.delete(player)
        session.commit()

@classmethod
def get_all(cls):
    return session.query(cls).all()

@classmethod
def find_by_id(cls, player_id):
    return session.query(cls).get(player_id)


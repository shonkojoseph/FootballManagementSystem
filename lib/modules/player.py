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

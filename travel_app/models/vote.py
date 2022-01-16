from sqlalchemy.orm import relationship
from travel_app.database.db import Base
from sqlalchemy import Column, Integer, ForeignKey

class Vote(Base):
    __tablename__ = 'votes'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    trek_destination_id = Column(Integer, ForeignKey('trek_destinations.trek_id', ondelete='CASCADE'), primary_key=True)
    votes = relationship('TrekDestination', back_populates='votes')
    voted_by = relationship('User')
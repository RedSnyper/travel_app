from travel_app.database.db import Base
from sqlalchemy import Column, Integer, ForeignKey

class Vote(Base):
    __tablename__ = 'votes'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    trek_destination_id = Column(Integer, ForeignKey('trek_destinations.id', ondelete='CASCADE'), primary_key=True)
     
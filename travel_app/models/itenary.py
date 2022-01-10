from sqlalchemy.orm import relationship
from travel_app.database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Itenary(Base):
    __tablename__ = 'iternaries'
    trek_destination_id = Column(Integer, ForeignKey("trek_destinations.id", ondelete='CASCADE'), primary_key=True)
    day = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    day_cost = Column(Integer, unique=True, nullable=False)
    itenaries = relationship('TrekDestination', back_populates='itenaries')

from sqlalchemy.orm import relationship
from travel_app.database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Itenary(Base):
    __tablename__ = 'iternaries'
    trek_destination_id = Column(Integer, ForeignKey("trek_destinations.trek_id", ondelete='CASCADE'), primary_key=True)
    day = Column(Integer, nullable=False, primary_key=True, )
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    day_cost = Column(Integer, nullable=False)
    itenaries = relationship('TrekDestination', back_populates='itenaries')


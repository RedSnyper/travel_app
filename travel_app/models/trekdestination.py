from sqlalchemy.sql.expression import text
from travel_app.database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

class TrekDestination(Base): #POST
    __tablename__ = "trek_destinations"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    days = Column(Integer, nullable=False)
    difficulty = Column(String, nullable=False, unique=True)
    total_cost = Column(Integer, unique=True, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    user_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'))
    owner = relationship("User", back_populates="trek_destination") #who wrote this trekdestination
    itenaries = relationship("Itenary", back_populates='trek_destination_id') #to get all iternaries of the trek destination
    comments = relationship("Comment", back_populates='comment_on') #to get all comment on the trek_destinations
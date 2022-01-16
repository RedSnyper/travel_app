from sqlalchemy.sql.expression import text
from travel_app.database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
class TrekDestination(Base): #POST
    __tablename__ = "trek_destinations"
    trek_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    days = Column(Integer, nullable=False)
    difficulty = Column(String, nullable=False)
    total_cost = Column(Integer, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    user_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'))
    created_by = relationship("User") #who wrote this trekdestination
    itenaries = relationship("Itenary", back_populates='itenaries') #to get all iternaries of the trek destination
    comments = relationship("Comment", back_populates='comments') #to get all comment on the trek_destinations
    votes = relationship('Vote', back_populates='votes')    #to get votes on the trekdestination

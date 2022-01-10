from sqlalchemy.sql.expression import text
from travel_app.database.db import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Comment(Base):
    __tablename__ ='comments'
    comment_on = Column(Integer, ForeignKey("trek_destinations.id", ondelete='CASCADE'), primary_key=True)
    comment_by = Column(Integer, ForeignKey("users.id", ondelete= 'CASCADE')) #subject to change to set null
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    

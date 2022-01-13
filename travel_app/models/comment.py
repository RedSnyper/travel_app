from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from travel_app.database.db import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Comment(Base):
    __tablename__ ='comments'
    id = Column(Integer, primary_key=True, nullable=False) #isnt there any elegant solution ? 
    comment_on = Column(Integer, ForeignKey("trek_destinations.id", ondelete='CASCADE'))
    comment_by = Column(Integer, ForeignKey("users.id", ondelete= 'CASCADE')) #subject to change to set null
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    comment = Column(String, nullable=False)

    comment_by_user = relationship('User') 
    comments = relationship('TrekDestination', back_populates='comments')   

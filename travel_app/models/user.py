from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from ..database import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP


class User(db.Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    full_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_no = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    # trek_destination = relationship('TrekDestination', back_populates="owner")

class TrekDestination(db.Base): #POST
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
    # owner = relationship("User", back_populates="trek_destination")

class Itenaries(db.Base):
    __tablename__ = 'iternaries'
    trek_destination_id = Column(Integer, ForeignKey("trek_destinations.id", ondelete='CASCADE'), primary_key=True)
    day = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    day_cost = Column(Integer, unique=True, nullable=False)
    # owner = relationship("User", back_populates="trek_destination")
 

class Comment(db.Base):
    __tablename__ ='comments'
    comment_on = Column(Integer, ForeignKey("trek_destinations.id", ondelete='CASCADE'), primary_key=True)
    comment_by = Column(Integer, ForeignKey("users.id", ondelete= 'CASCADE')) #subject to change to set null
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class Upvote(db.Base):
    __tablename__ = 'votes'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    trek_destination_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'), primary_key=True)
     
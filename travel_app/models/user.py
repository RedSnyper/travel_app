from sqlalchemy.sql.expression import text
from travel_app.database.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    full_name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    phone_no = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    routes_written = relationship('TrekDestination', back_populates="created_by") #to get all trekdestinations posted by this user
    # comments_written = relationship('Comment', back_populates='comment_by_user')




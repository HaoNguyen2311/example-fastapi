from .database import Base
from sqlalchemy import Column, Integer,String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

# in first time run if this table doesn't exist it will be create, but it already exist it can not update or touch.
class Post(Base):
  # define name of table
  __tablename__ = 'posts'
  
  # define columns
  id = Column(Integer, primary_key = True, nullable = False)
  title = Column(String, nullable = False)
  content = Column(String, nullable = False)
  published = Column(Boolean, server_default = 'TRUE',nullable = False) 
  create_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))
  user_id = Column(Integer,ForeignKey('user.id',ondelete="CASCADE") ,nullable = False)
  
  #  owner = relationship('class User')
  owner = relationship('User')
  
class User(Base):
  __tablename__ = 'user'
  
  id = Column(Integer, primary_key = True, nullable = False)
  email = Column(String, nullable = False, unique = True)
  password = Column(String, nullable = False)
  create_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))
  phone_number = Column(String, nullable = False)
  
class Vote(Base):
  __tablename__ = 'votes'
  # user.id is reference with user table 
  user_id = Column(Integer, ForeignKey('user.id',ondelete="CASCADE"), primary_key = True) 
  post_id = Column(Integer, ForeignKey('posts.id',ondelete="CASCADE"), primary_key = True) 

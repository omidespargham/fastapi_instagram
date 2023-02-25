from db.database import Base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    password = Column(String) # Body(regex)
    email = Column(String) # you can normalize your email with Body(regex)
    user_posts = relationship("Post",back_populates="user")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer,ForeignKey("users.id"))
    user = relationship("User",back_populates="user_posts")
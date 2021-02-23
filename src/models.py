import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)


class Follower(Base):
    __tablename__= 'follower'
    id = Column(Integer, primary_key=True)
    userFromId = Column(Integer, ForeignKey('user.id'))
    userToId = Column(Integer, ForeignKey('user.id'))


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'))


class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    postId = Column(Integer, ForeignKey('post.id'))
    userId = Column(Integer, ForeignKey('user.id'))


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    mediaType = Column(String(50), nullable=False)
    url = Column(String(250), nullable=False)
    postId = Column(Integer, ForeignKey('post.id'))


class Comment(Base):
    __tablename__= 'comment'
    id = Column(Integer, primary_key=True)
    commentText = Column(String(250), nullable=False)
    authorId = Column(Integer, ForeignKey('user.id'))
    postId = Column(Integer, ForeignKey('post.id'))
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table # type: ignore
from sqlalchemy.orm import relationship, declarative_base # type: ignore
from sqlalchemy import create_engine # type: ignore
from eralchemy2 import render_er  # type: ignore 

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(30), unique=True, nullable=False)
    favorite = relationship('Favorite', backref='user', lazy=True)
 

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50))
    terrain = Column(String(50))
    population = Column(Integer)
    favorite = relationship('Favorite', backref='planet', lazy=True)
   

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(10))
    favorite = relationship('Favorite', backref='character', lazy=True)
  

class Favorite(Base):
    __tablename__='favorite'
    id= Column (Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'),nullable=False)
    planet_id = Column(Integer,ForeignKey('planet.id'),nullable=True)
    character_id = Column(Integer,ForeignKey('character.id'),nullable=True)


render_er(Base, 'diagram.png')


#!/usr/bin/python3
"""
Module to define user
"""
from flask_login import UserMixin
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()



class User(BaseModel, Base, UserMixin):
    """class user"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        username = Column(String(128), nullable=False)
        phone_number = Column(String(15), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = relationship("Review", backref="users")
    else:
        phone_number = ""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        username = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        '''if name == "password":
            hashed_password = bcrypt.generate_password_hash(value).decode('utf-8')
            value = hashed_password'''
        super().__setattr__(name, value)

#!/usr/bin/python3
"""
Module to define user
"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """class user"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        phone_number = Column(String(15), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=True)
        user_name = Column(String(128), nullable=True)
        reviews = relationship("Review", backref="users")
    else:
        phone_number = ""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        user_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

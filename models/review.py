#!/usr/bin/python3
"""class to define reviews table"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey


class Review(BaseModel, Base):
    """review class definition"""
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        user_id = ""
        text = ""


    def __init__(self, *args, **kwargs):
        """ class initialization"""
        super().__init__(*args, **kwargs)

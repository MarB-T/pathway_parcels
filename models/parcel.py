#!/usr/bin/python3
""" parcel definition """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Table


class Parcel(BaseModel, Base):
    """parcel class"""
    if models.storage_t == 'db':
        __tablename__ = 'parcels'
        parcel_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, default=99)
        sender_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        origin = Column(String(60), nullable=False)
        destination = Column(String(60), nullable=False)
        size_l_cm = Column(Integer, nullable=False, default=10)
        size_w_cm = Column(Integer, nullable=False, default=10)
        size_h_cm = Column(Integer, nullable=False, default=10)
        weight_kg = Column(Integer, nullable=False, default=1)
        offered_amount = Column(Integer, nullable=False, default=100)
    else:
        parcel_id = ""
        sender_id = ""
        origin = ""
        destination = ""
        size_l_cm = 10
        size_w_cm = 10
        size_h_cm = 10
        weight_kg = 1
        offered_amount = 100

    def __init__(self, *args, **kwargs):
        """initialize parcel"""
        super().__init__(*args, **kwargs)

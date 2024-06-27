#!/usr/bin/python3
"""Amenity module for the HBNB project"""

from models.base_model import BaseModel, Base
from models import HBNB_TYPE_STORAGE
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity class to store amenity information"""
    __tablename__ = 'amenities'

    if HBNB_TYPE_STORAGE == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""

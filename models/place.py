#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base



class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(
        String(60), nullable=False, ForeignKey('cities.id')
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    user_id = Column(
        String(60), nullable=False, ForeignKey('users.id')
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    description = Column(
        String(1024), nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    number_rooms = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0

    number_bathrooms = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0


    max_guest = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0

    price_by_night = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0

    latitude = Column(
        Float, nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0

    longitude = Column(
        Float, nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0


    amenity_ids = []

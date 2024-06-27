#!/usr/bin/python3
""" Place Module for HBNB project """

from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from models import HBNB_TYPE_STORAGE
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if HBNB_TYPE_STORAGE == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place', cascade='all, delete')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 backref='place_amenities', viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            '''Returns a list of review instances with place_id
                equal to the current Place.id.
            '''
            from models import storage
            return [rev for rev in storage.all(Review).values()
                    if rev.place_id == self.id]

        @property
        def amenities(self):
            '''Returns a list of Amenity instances linked to the Place.'''
            from models import storage
            return [amen for amen in storage.all(Amenity).values()
                    if amen.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            '''Adds an Amenity.id to the attribute amenity_ids.
                Accepts only Amenity objects.
            '''
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)

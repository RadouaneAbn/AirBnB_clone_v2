#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from os import environ
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        """ When using a DBStorage """
        reviews = relationship("Review",
                               cascade="all, delete, delete-orphan",
                               backref="place")
    else:
        """ When using a FileStorage """
        @property
        def reviews(self):
            list_reviews = []
            from models import storage
            all_inst = storage.all("Review")
            for key, value in all_inst.items():
                list_reviews.append(value)
            return list_reviews

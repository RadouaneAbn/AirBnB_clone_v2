#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import environ
from sqlalchemy.orm import relationship

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id',
           String(60),
           ForeignKey('places.id'),
           primary_key=True,
           nullable=False),
    Column('amenity_id',
           String(60),
           ForeignKey('amenities.id'),
           primary_key=True,
           nullable=False)
)


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
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        """ When using a FileStorage """
        @property
        def reviews(self):
            list_reviews = []
            from models import storage
            all_inst = storage.all("Review")
            for key, value in all_inst.items():
                if (self.id == value.id):
                    list_reviews.append(value)
            return list_reviews

        @property
        def amenities(self):
            list_amenities = []
            from models import storage
            all_inst = storage.all("Amenity")
            for k, v in all_inst.items():
                if v.id in self.amenity_ids:
                    list_amenities.append(v)
            return list_amenities

        @amenities.setter
        def amenities(self, obj=None):
            if obj.__class__ != "Amenity":
                return

            self.amenity_ids.append(obj.id)

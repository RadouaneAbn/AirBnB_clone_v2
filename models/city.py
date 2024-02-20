#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullbale=False)
    name = Column(String(128), nullbale=False)
    Places = relationship("Place", cascade='all, delete, delete-orphan', backref="cities")

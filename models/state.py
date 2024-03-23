#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, MetaData, Table, DateTime

from os import environ

# metadata = MetaData()
# states = Table('places', metadata,
#                Column(String(60), unique=True, nullable=False, primary_key=True),
#                Column(DateTime, default=datetime.now(), nullable=False)
#             Column(DateTime, default=datetime.now(), nullable=False)
# )


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade="all, delete-orphan")


    if not environ.get('HBNB_TYPE_STORAGE') == "db":
        @property
        def cities(self):
            from models import storage
            cities_list = [city for _, city in storage.all("City").items()
                           if city.state_id == self.id]
            return cities_list
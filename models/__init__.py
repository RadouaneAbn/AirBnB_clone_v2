#!/usr/bin/python3
from os import environ

if environ.get('HBNB_TYPE_STORAGE') == "db":
    """ Use DBStorage"""
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    """ Use FileStorage """
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()

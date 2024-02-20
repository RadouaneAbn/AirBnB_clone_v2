#!/usr/bin/python3
from os import environ

if environ.get('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    print("db called")
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    
storage.reload()
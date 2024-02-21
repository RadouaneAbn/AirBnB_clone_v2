#!/usr/bin/python3
""" db_storage Module"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from sqlalchemy import inspect
from os import environ
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ Create an engine """
        mysql_user = environ.get('HBNB_MYSQL_USER')
        mysql_password = environ.get('HBNB_MYSQL_PWD')
        mysql_host = environ.get('HBNB_MYSQL_HOST')
        mysql_db = environ.get('HBNB_MYSQL_DB')
        # print("creating engine")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            mysql_user, mysql_password, mysql_host, mysql_db),
            pool_pre_ping=True)

        # print("engine created")
        if environ.get('HBNB_ENV') == 'test':
            table_names = inspect(self.__engine).get_table_names()

            for table_name in table_names:
                table = Base.metadata.tables[table_name]
                table.drop(self.__engine)

    def reload(self):
        """ Create a Session """
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def new(self, obj):
        """ Add new inst into Session """
        attrs = obj.to_dict()
        # print("attrs are: ", attrs)
        cls = obj.__class__
        new_instance = cls()
        for key, value in attrs.items():
            if key == "__class__":
                continue
            setattr(new_instance, key, value)
        # print("new inst is : ", new_instance)
        self.__session.add(new_instance)

    def save(self):
        """ Commit the changes into the data base """
        self.__session.commit()

    def all(self, cls=None):
        """ Return a dictionary of instances """
        classes = {
            "State": State,
            "City": City,
            "User": User,
            "Place": Place,
            # "Review": Review,
            # "Amenity": Amenity,
        }
        table_to_class = {
            'states': State,
            'cities': City,
            'users': User,
            'places': Place
        }
        dictionary = {}
        inst_attr = {}
        attrs_list = []

        if cls:
            table = Base.metadata.tables[classes[cls].__tablename__]
            for inst in self.__session.query(table).all():
                inst_attr = {
                    column.name: getattr(inst, column.name)
                    for column in table.columns if not hasattr(
                        inst, "_sa_instance_state")
                }
                attrs_list.append((classes[cls], inst_attr))
        else:
            table_names = inspect(self.__engine).get_table_names()
            for table_name in table_names:
                table = Base.metadata.tables[table_name]
                for inst in self.__session.query(table).all():
                    inst_attr = {
                        column.name: getattr(inst, column.name)
                        for column in table.columns if not hasattr(
                            inst, "_sa_instance_state")
                    }
                    class_obj = table_to_class[table_name]
                    attrs_list.append((class_obj, inst_attr))

        for Class, attr in attrs_list:
            # print("attrs :", attr)
            new_instance = Class(**attr)
            # print("#############################")
            # print("inst: ", new_instance)
            # print("#############################")
            key, value = f"{Class.__name__}.{new_instance.id}", new_instance
            # print("key: ", key)
            # print("value: ", value)
            dictionary[key] = value

        # print("dict is ==> \n", dictionary)
        return dictionary

    def delete(self, obj=None):
        """ Deletes an instance from a database """
        classes = {
            "states": State,
            "cities": City,
            "users": User,
            "places": Place,
            # "Review": Review,
            # "Amenity": Amenity,
        }
        if not obj:
            return

        # print(type(obj))
        # print("obj: \n", obj)
        table = Base.metadata.tables[obj.__tablename__]
        # print("table =======> ", table)
        cls = classes[str(table)]
        # print(cls)
        wanted_row = self.__session.query(cls)\
            .where(cls.id == obj.id).one_or_none()
        # print("wanted: \n==> ", wanted_row)
        if not wanted_row:
            return

        self.__session.delete(wanted_row)
        self.__session.commit()

#!/usr/bin/python3
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from sqlalchemy import inspect
from os import environ


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        mysql_user = environ.get('HBNB_MYSQL_USER')
        mysql_password = environ.get('HBNB_MYSQL_PWD')
        mysql_host = environ.get('HBNB_MYSQL_HOST')
        mysql_db = environ.get('HBNB_MYSQL_DB')
        print("creating engine")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'\
            .format(mysql_user, mysql_password, mysql_host, mysql_db),
            pool_pre_ping=True)
        
        print("engine created")
        if environ.get('HBNB_ENV') == 'test':
            table_names = inspect(self.__engine).get_table_names()

            for table_name in table_names:
                table = Base.metadata.tables[table_name]
                table.drop(self.__engine)
                

    def reload(self):
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()



    def new(self, obj):
        attrs = obj.to_dict()
        print("attrs are: ", attrs)
        cls = obj.__class__
        new_instance = cls()
        for key, value in attrs.items():
            if key == "__class__":
                continue
            setattr(new_instance, key, value)
        # print("new inst is : ", new_instance)
        self.__session.add(new_instance)

    def save(self):
        self.__session.commit()

    def all(self, cls=None):
        
        if cls:
            self.__session.query(cls).all()
        else:
            table_names = inspect(self.__engine).get_table_names()

            for table_name in table_names:
                table = Base.metadata.tables[table_name]
                for row in self.__session.query(table).all():
                    print(row)


    def delete(self, obj=None):
        if not obj:
            return
        
        wanted_row = self.__session.query(obj.__tablename__).where(id=obj.id)
        if not wanted_row:
            return
        
        self.__session.delete(wanted_row)
        self.__session.commit()
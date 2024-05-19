#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb evolution"""

import importlib
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage():
    """ Class for reading data from databases """
    __engine = None
    __session = None
    __module_names = {
        "User": "user",
        "Country": "country",
        "City": "city",
        "Amenity": "amenity",
        "Place": "place",
        "Review": "review"
    }

    def __init__(self, Base):
        """Instantiate a DBStorage object"""
        self.__base = Base

        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        is_testing = getenv('TESTING')

        # If you were lazy and didn't specify anything on the command line, then the defaults below will be used
        # PLEASE DON'T DO THIS IN A REAL WORKING ENVIRONMENT
        if user is None:
            user = "hbnb_evo"
        if pwd is None:
            pwd = "hbnb_evo_pwd"
        if host is None:
            host = "localhost"
        if db is None:
            if is_testing == "1":
                db = "hbnb_test_db"
            else:
                db = "hbnb_evo_db"

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db))

        if is_testing == "1":
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def get(self, class_name = "", record_id = ""):
        """ Return all data or data for specified class name and / or id"""

        if class_name == "":
            raise IndexError("Unable to load Model data. No class name specified")

        if not self.__module_names[class_name]:
            raise IndexError("Unable to load Model data. Specified class name not found")

        namespace = self.__module_names[class_name]
        module = importlib.import_module("models." + namespace)
        class_ = getattr(module, class_name)

        if record_id == "":
            rows = self.__session.query(class_).all()
        else:
            try:
                rows = self.__session.query(class_).where(class_.id == record_id).limit(1).one()
            except:
                raise IndexError("Unable to load Model data. Specified id not found")

        return rows

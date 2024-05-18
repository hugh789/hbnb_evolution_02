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
    __data = {}
    __base = None
    __module_names = {
        "BaseModel": "base_model",
        "User": "user",
        "State": "state",
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
            user = "hbnb_dev"
        if pwd is None:
            pwd = "hbnb_dev_pwd"
        if host is None:
            host = "localhost"
        if db is None:
            if is_testing == "1":
                db = "hbnb_test_db"
            else:
                db = "hbnb_dev_db"

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

        namespace = self.__module_names[class_name]
        module = importlib.import_module("models." + namespace)
        class_ = getattr(module, class_name)
        rows = self.__session.query(class_).all()

        return rows

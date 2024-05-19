#!/usr/bin/python

from datetime import datetime
import uuid
import re
from flask import jsonify, request, abort
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from data import storage, use_db_storage, Base

class City():
    """Representation of city """

    # Class attrib defaults
    id = None
    created_at = None
    updated_at = None
    __name = ""
    __country_id = ""

    if use_db_storage:
        __tablename__ = 'cities'
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.now().timestamp())
        updated_at = Column(DateTime, nullable=False, default=datetime.now().timestamp())
        __name = Column("name", String(128), nullable=False)
        __country_id = Column("country", String(2), nullable=False)
        country = relationship("Country", back_populates="cities")

    # constructor
    def __init__(self, *args, **kwargs):
        """ constructor """
        # Set object instance defaults
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at

        # Only allow country_id, name.
        # Note that setattr will call the setters for these 2 attribs
        if kwargs:
            for key, value in kwargs.items():
                if key in ["country_id", "name"]:
                    setattr(self, key, value)

    @property
    def name(self):
        """Getter for private prop name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for private prop name"""

        # ensure that the value is not spaces-only and is alphabets + spaces only
        is_valid_name = len(value.strip()) > 0 and re.search("^[a-zA-Z ]+$", value)
        if is_valid_name:
            self.__name = value
        else:
            raise ValueError("Invalid city name specified: {}".format(value))

    @property
    def country_id(self):
        """Getter for private prop country_id"""
        return self.__country_id

    @country_id.setter
    def country_id(self, value):
        """Setter for private prop country_id"""

        # ensure that the specified country id actually exists before setting
        if country_data.get(value) is not None:
            self.__country_id = value
        else:
            raise ValueError("Invalid country_id specified: {}".format(value))

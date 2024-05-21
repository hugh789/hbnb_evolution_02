#!/usr/bin/python3
""" initialize the storage used by models """

import os
from data.db_storage import DBStorage
from data.file_storage import FileStorage
from sqlalchemy.ext.declarative import declarative_base

# check for STORAGE=FILE from command line
# command to use: STORAGE=FILE python3 ./app.py
USE_DB_STORAGE = True
if "STORAGE" in os.environ and os.environ['STORAGE'] == "FILE":
    USE_DB_STORAGE = False

# check for TESTING=1 from command line
# command to use: TESTING=1 python3 -m unittest discover
is_testing = "TESTING" in os.environ and os.environ['TESTING'] == "1"

# Note that we are creating object instances of the Storage classes
# Each storage object could have different settings that affect loading/saving of data.
if USE_DB_STORAGE:
    Base = declarative_base()
    storage = DBStorage(Base)
else:
    Base = object
    storage = FileStorage()
    storage.load_data(is_testing)

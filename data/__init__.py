#!/usr/bin/python3
""" initialize the storage used by models """

import os
from data.db_storage import DBStorage
from data.file_storage import FileStorage

# check for STORAGE=FILE from command line
# command to use: STORAGE=FILE python3 ./app.py
use_file_storage = "STORAGE" in os.environ and os.environ['STORAGE'] == "FILE"

# check for TESTING=1 from command line
# command to use: TESTING=1 python3 -m unittest discover
is_testing = "TESTING" in os.environ and os.environ['TESTING'] == "1"

all_data = {}

if use_file_storage:
    storage = FileStorage()
else:
    storage = DBStorage()

all_data = storage.load_data(is_testing)

country_data = all_data['models']['Country']
city_data = all_data['models']['City']
amenity_data = all_data['models']['Amenity']
place_data = all_data['models']['Place']
user_data = all_data['models']['User']
review_data = all_data['models']['Review']
place_to_amenity_data = all_data['relations']['Place']['Amenity']

#!/usr/bin/python

from datetime import datetime
import uuid
import re
from flask import jsonify, request, abort
from data import storage

class Country():
    """Representation of country """

    # Constructor
    def __init__(self, *args, **kwargs):
        """ constructor """
        # super().__init__(*args, **kwargs)

        # defaults
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at
        self.__name = ""
        self.__code = ""

        # Only allow name, code.
        # Note that setattr will call the setters for these attribs
        if kwargs:
            for key, value in kwargs.items():
                if key == "name" or key == "code":
                    setattr(self, key, value)

    # --- Getters and Setters ---
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
            raise ValueError("Invalid country name specified: {}".format(value))

    @property
    def code(self):
        """Getter for private prop code"""
        return self.__code

    @code.setter
    def code(self, value):
        """Setter for private prop code"""

        # ensure that the value is not spaces-only and is two uppercase alphabets only
        is_valid_code = len(value.strip()) > 0 and re.search("^[A-Z][A-Z]$", value)
        if is_valid_code:
            self.__code = value
        else:
            raise ValueError("Invalid country code specified: {}".format(value))

    # --- Static methods ---
    @staticmethod
    def all():
        """ Class method that returns all countries data"""
        data = []
        country_data = storage.get("Country")

        for k, v in country_data.items():
            data.append({
                "id": v['id'],
                "name": v['name'],
                "code": v['code'],
                "created_at": datetime.fromtimestamp(v['created_at']),
                "updated_at": datetime.fromtimestamp(v['updated_at'])
            })

        return jsonify(data)

    @staticmethod
    def specific(country_code):
        """ Class method that returns a specific country's data"""
        country_data = storage.get("Country")

        for k, v in country_data.items():
            if v['code'] == country_code:
                data = v

        c = {
            "id": data['id'],
            "name": data['name'],
            "code": data['code'],
            "created_at": datetime.fromtimestamp(data['created_at']),
            "updated_at": datetime.fromtimestamp(data['updated_at'])
        }

        return jsonify(c)

    @staticmethod
    def create():
        """ Class method that creates a new country"""
        # -- Usage example --
        # curl -X POST [URL] /
        #    -H "Content-Type: application/json" /
        #    -d '{"key1":"value1","key2":"value2"}'

        if request.get_json() is None:
            abort(400, "Not a JSON")

        data = request.get_json()
        if 'name' not in data:
            abort(400, "Missing name")
        if 'code' not in data:
            abort(400, "Missing country code")

        try:
            c = Country(name=data["name"],code=data["code"])
        except ValueError as exc:
            return repr(exc) + "\n"

        attribs = {
            "id": c.id,
            "name": c.name,
            "code": c.code,
            "created_at": c.created_at,
            "updated_at": c.updated_at
        }

        # add to whatever is in storage at the moment
        storage.add('Country', attribs)

        # print the Users out and you'll see the new one has been added
        # print(storage.get('Country'))

        # update the created_at and updated_at to something readable before passing it out for display
        attribs['created_at'] = datetime.fromtimestamp(c.created_at)
        attribs['updated_at'] = datetime.fromtimestamp(c.updated_at)

        return jsonify(attribs)

    @staticmethod
    def update(country_code):
        """ Class method that updates an existing country"""
        # -- Usage example --
        # curl -X PUT [URL] /
        #    -H "Content-Type: application/json" /
        #    -d '{"key1":"value1","key2":"value2"}'

        c = {}

        if request.get_json() is None:
            abort(400, "Not a JSON")

        data = request.get_json()
        country_data = storage.get("Country")

        for k, v in country_data.items():
            if v['code'] == country_code:
                c = v

        if not c:
            abort(400, "Country not found for code {}".format(country_code))

        # modify the values
        # only name is allowed to be modified
        for k, v in data.items():
            if k in ["name"]:
                c[k] = v

        attribs = {
            "id": c["id"],
            "name": c["name"],
            "code": c["code"],
            "created_at": c["created_at"],
            "updated_at": c["updated_at"]
        }

        country_id = c["id"]

        # update the Country records with the new name
        storage.update('Country', country_id, attribs)

        # print the Users out and you'll see the record has been updated
        # print(storage.get('Country'))

        attribs['created_at'] = datetime.fromtimestamp(c["created_at"])
        attribs['updated_at'] = datetime.fromtimestamp(c["updated_at"])

        # print out the updated user details
        return jsonify(attribs)

    @staticmethod
    def cities(country_code):
        """ Class method that returns a specific country's cities"""
        data = []
        wanted_country_id = ""

        country_data = storage.get("Country")
        city_data = storage.get("City")

        for k, v in country_data.items():
            if v['code'] == country_code:
                wanted_country_id = v['id']

        for k, v in city_data.items():
            if v['country_id'] == wanted_country_id:
                data.append({
                    "id": v['id'],
                    "name": v['name'],
                    "country_id": v['country_id'],
                    "created_at":datetime.fromtimestamp(v['created_at']),
                    "updated_at":datetime.fromtimestamp(v['updated_at'])
                })

        return jsonify(data)

#!/usr/bin/python3

from flask import Flask
from models.country import Country
from models.user import User

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Hello world """
    return 'Hello World'

@app.route('/', methods=["POST"])
def hello_world_post():
    """ Hello world endpoint for POST requests """
    # curl -X POST localhost:5000/
    return "hello world\n"


# --- API endpoints ---
# --- USER ---
@app.route('/api/v1/users', methods=["GET"])
def users_get():
    """returns Users"""
    # use the User class' static .all method
    return User.all()

@app.route('/api/v1/users/<user_id>', methods=["GET"])
def users_specific_get(user_id):
    """returns specified user"""
    # use the User class' static .specific method
    return User.specific(user_id)

@app.route('/api/v1/users', methods=["POST"])
def users_post():
    """ posts data for new user then returns the user data"""
    # use the User class' static .create method
    return User.create()

@app.route('/api/v1/users/<user_id>', methods=["PUT"])
def users_put(user_id):
    """ updates existing user data using specified id """
    # use the User class' static .update method
    return User.update(user_id)


# --- COUNTRY ---
@app.route('/api/v1/countries', methods=["POST"])
def countries_post():
    """ posts data for new country then returns the country data"""
    return Country.create()

@app.route('/api/v1/countries', methods=["GET"])
def countries_get():
    """ returns countires data """
    return Country.all()

@app.route('/api/v1/countries/<country_code>', methods=["GET"])
def countries_specific_get(country_code):
    """ returns specific country data """
    return Country.specific(country_code)

@app.route('/api/v1/countries/<country_code>', methods=["PUT"])
def countries_put(country_code):
    """ updates existing user data using specified id """
    return Country.update(country_code)

@app.route('/api/v1/countries/<country_code>/cities', methods=["GET"])
def countries_specific_cities_get(country_code):
    """ returns cities data of specified country """
    return Country.cities(country_code)

# Create the rest of the endpoints for:
#  - City
#  - Amenity
#  - Place
#  - Review


# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

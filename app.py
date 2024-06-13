#!/usr/bin/python3

from flask import Flask, jsonify
from models.country import Country
from models.user import User
from data import USE_DB_STORAGE

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

# Examples - These will only work with DB Storage!
# We're using the power of relationships to grab the data we need!
@app.route('/example/places_amenities')
def places_amenities_get():
    """ gives any example of how to use relationships to access data """
    # NOTE: This example will only work with the data in the DB
    from data import storage, USE_DB_STORAGE
    from models.place_amenity import Place

    place_amenities = {}
    amenities_list = []
    if USE_DB_STORAGE:
        place_id = "71bebd9b-481b-4bf0-bb83-4e30ea66bdaa"
        specific_place = storage.get('Place', place_id)

        for item in specific_place.amenities:
            amenities_list.append(item.name)

        place_amenities[specific_place.name] = amenities_list

    return place_amenities

@app.route('/example/amenities_places')
def amenities_places_get():
    """ gives any example of how to use relationships to access data """
    # NOTE: This example will only work with the data in the DB
    from data import storage, USE_DB_STORAGE
    from models.place_amenity import Amenity

    amenity_places = {}
    places_list = []
    if USE_DB_STORAGE:
        amenity_id = "2ec8cf22-e5ea-4a1f-aedd-89f15fcc60e9"
        specific_amenity = storage.get('Amenity', amenity_id)

        for item in specific_amenity.places:
            places_list.append(item.name)

        amenity_places[specific_amenity.name] = places_list

    return amenity_places

@app.route('/example/malaysia_cities')
def malaysia_cities_get():
    """ Example to show how to get cities data for a country using relationships """
    from data import storage, USE_DB_STORAGE

    # Output is equivalent to http://localhost:5000/api/v1/countries/MY/cities

    data = []
    if USE_DB_STORAGE:
        country_id = "db63e499-f604-41a3-b97a-ee4bf9331f75"
        result = storage.get('Country', country_id)

        # Note the use of the cities relationship
        city_data = result.cities
        for v in city_data:
            data.append({
                "id": v.id,
                "name": v.name,
                "country_id": v.country_id,
                "created_at":v.created_at.strftime(Country.datetime_format),
                "updated_at":v.updated_at.strftime(Country.datetime_format)
            })

    return data

@app.route('/example/kuala_lumpur_parent_country')
def kl_parent_country_get():
    """ Example to show how to get country data for a city using relationships """
    from data import storage, USE_DB_STORAGE

    output = ""
    if USE_DB_STORAGE:
        city_id = "68c06ef5-bf33-46df-a894-9ac54f728f43"
        city_obj = storage.get('City', city_id)

        # Note the use of the country relationship
        country = city_obj.country

        output = city_obj.name + ' is a city in ' + country.name + '!!'

    return output


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
    # -- Usage example --
    # curl -X POST localhost:5000/api/v1/users /
    #   -H "Content-Type: application/json" /
    #   -d '{"first_name":"Peter","last_name":"Parker","email":"p.parker@daily-bugle.net","password":"123456"}'

    # use the User class' static .create method
    return User.create()

@app.route('/api/v1/users/<user_id>', methods=["PUT"])
def users_put(user_id):
    """ updates existing user data using specified id """
    # -- Usage example --
    # curl -X PUT [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    # use the User class' static .update method
    # can only update first_name and last_name
    return User.update(user_id)


# --- COUNTRY ---
@app.route('/api/v1/countries', methods=["POST"])
def countries_post():
    """ posts data for new country then returns the country data"""
    # -- Usage example --
    # curl -X POST [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

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
    # -- Usage example --
    # curl -X PUT [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    # can only update name
    return Country.update(country_code)

@app.route('/api/v1/countries/<country_code>/cities', methods=["GET"])
def countries_specific_cities_get(country_code):
    """ returns cities data of specified country """
    return Country.cities_data(country_code)

# Create the rest of the endpoints for:
#  - City
#  - Amenity
#  - Place
#  - Review


# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

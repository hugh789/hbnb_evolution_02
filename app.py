#!/usr/bin/python3

from datetime import datetime
from flask import Flask, jsonify, request, abort
from models.user import User
from data import all_data

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Hello world """
    return 'Hello World'

# # --- API endpoints ---
# # --- USER ---
# @app.route('/api/v1/users', methods=["GET"])
# def users_get():
#     """returns Users"""
#     data = []

#     for k, v in user_data.items():
#         data.append({
#             "id": v['id'],
#             "first_name": v['first_name'],
#             "last_name": v['last_name'],
#             "email": v['email'],
#             "password": v['password'],
#             "created_at": v['created_at'],
#             "updated_at": v['updated_at']
#         })

#     return jsonify(data)

# @app.route('/api/v1/users/<user_id>', methods=["GET"])
# def users_specific_get(user_id):
#     """returns specified user"""
#     data = []

#     if user_id not in user_data:
#         # raise IndexError("User not found!")
#         return "User not found!"

#     v = user_data[user_id]
#     data.append({
#         "id": v['id'],
#         "first_name": v['first_name'],
#         "last_name": v['last_name'],
#         "email": v['email'],
#         "password": v['password'],
#         "created_at": v['created_at'],
#         "updated_at": v['updated_at']
#     })
#     return jsonify(data)

# @app.route('/api/v1/users', methods=["POST"])
# def users_post():
#     """ posts data for new user then returns the user data"""
#     # -- Usage example --
#     # curl -X POST [URL] /
#     #    -H "Content-Type: application/json" /
#     #    -d '{"key1":"value1","key2":"value2"}'

#     # print(request.content_type)

#     if request.get_json() is None:
#         abort(400, "Not a JSON")

#     data = request.get_json()
#     if 'email' not in data:
#         abort(400, "Missing email")
#     if 'password' not in data:
#         abort(400, "Missing password")

#     try:
#         u = User(first_name=data["first_name"],last_name=data["last_name"], email=data["email"], password=data["password"])
#     except ValueError as exc:
#         return repr(exc) + "\n"

#     attribs = {
#         "id": u.id,
#         "first_name": u.first_name,
#         "last_name": u.last_name,
#         "email": u.email,
#         "created_at": datetime.fromtimestamp(u.created_at),
#         "updated_at": datetime.fromtimestamp(u.updated_at)
#     }

#     return jsonify(attribs)

# @app.route('/api/v1/users/<user_id>', methods=["PUT"])
# def users_put(user_id):
#     """ updates existing user data using specified id """
#     # -- Usage example --
#     # curl -X PUT [URL] /
#     #    -H "Content-Type: application/json" /
#     #    -d '{"key1":"value1","key2":"value2"}'

#     if request.get_json() is None:
#         abort(400, "Not a JSON")

#     data = request.get_json()

#     if user_id not in user_data:
#         abort(400, "User not found for id {}".format(user_id))

#     u = user_data[user_id]

#     # modify the values
#     for k, v in data.items():
#         # only first_name and last_name are allowed to be modified
#         if k in ["first_name", "last_name"]:
#             u[k] = v

#     # update user_data with the new name - print user_data out to confirm it if you
#     user_data[user_id] = u

#     v = user_data[user_id]
#     attribs = {
#         "id": v["id"],
#         "first_name": v["first_name"],
#         "last_name": v["last_name"],
#         "email": v["email"],
#         "created_at": datetime.fromtimestamp(v["created_at"]),
#         "updated_at": datetime.fromtimestamp(v["updated_at"])
#     }

#     # print out the updated user details
#     return jsonify(attribs)

# # --- COUNTRY ---
# @app.route('/api/v1/countries', methods=["POST"])
# def countries_post():
#     """ posts data for new country then returns the country data"""
#     # -- Usage example --
#     # curl -X POST [URL] /
#     #    -H "Content-Type: application/json" /
#     #    -d '{"key1":"value1","key2":"value2"}'

#     if request.get_json() is None:
#         abort(400, "Not a JSON")

#     data = request.get_json()
#     if 'name' not in data:
#         abort(400, "Missing name")
#     if 'code' not in data:
#         abort(400, "Missing country code")

#     try:
#         c = Country(name=data["name"],code=data["code"])
#     except ValueError as exc:
#         return repr(exc) + "\n"

#     attribs = {
#         "id": c.id,
#         "name": c.name,
#         "code": c.code,
#         "created_at": datetime.fromtimestamp(c.created_at),
#         "updated_at": datetime.fromtimestamp(c.updated_at)
#     }

#     return jsonify(attribs)

# @app.route('/api/v1/countries', methods=["GET"])
# def countries_get():
#     """ returns countires data """
#     data = []

#     for k, v in country_data.items():
#         data.append({
#             "id": v['id'],
#             "name": v['name'],
#             "code": v['code'],
#             "created_at": v['created_at'],
#             "updated_at": v['updated_at']
#         })

#     return jsonify(data)

# @app.route('/api/v1/countries/<country_code>', methods=["GET"])
# def countries_specific_get(country_code):
#     """ returns specific country data """
#     c = {}

#     for k, v in country_data.items():
#         if v['code'] == country_code:
#             data = v

#     return jsonify(data)

# @app.route('/api/v1/countries/<country_code>', methods=["PUT"])
# def countries_put(country_code):
#     """ updates existing user data using specified id """
#     # -- Usage example --
#     # curl -X PUT [URL] /
#     #    -H "Content-Type: application/json" /
#     #    -d '{"key1":"value1","key2":"value2"}'

#     c = {}

#     if request.get_json() is None:
#         abort(400, "Not a JSON")

#     data = request.get_json()
#     for k, v in country_data.items():
#         if v['code'] == country_code:
#             c = v

#     if not c:
#         abort(400, "Country not found for code {}".format(country_code))

#     # modify the values
#     # only name is allowed to be modified
#     for k, v in data.items():
#         if k in ["name"]:
#             c[k] = v

#     # update country_data with the new name - print country_data out to confirm it if you
#     country_data[c['id']] = c

#     attribs = {
#         "id": c["id"],
#         "name": c["name"],
#         "code": c["code"],
#         "created_at": datetime.fromtimestamp(c["created_at"]),
#         "updated_at": datetime.fromtimestamp(c["updated_at"])
#     }

#     # print out the updated user details
#     return jsonify(attribs)

# @app.route('/api/v1/countries/<country_code>/cities', methods=["GET"])
# def countries_specific_cities_get(country_code):
#     """ returns cities data of specified country """
#     data = []
#     wanted_country_id = ""

#     for k, v in country_data.items():
#         if v['code'] == country_code:
#             wanted_country_id = v['id']

#     for k, v in city_data.items():
#         if v['country_id'] == wanted_country_id:
#             data.append({
#                 "id": v['id'],
#                 "name": v['name'],
#                 "country_id": v['country_id'],
#                 "created_at": v['created_at'],
#                 "updated_at": v['updated_at']
#             })

#     return jsonify(data)

# Create the rest of the endpoints for:
#  - City
#  - Amenity
#  - Place
#  - Review


# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

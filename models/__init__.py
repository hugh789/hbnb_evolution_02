from flask import jsonify, request, abort
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from data import storage, USE_DB_STORAGE, Base

place_amenity = None
if USE_DB_STORAGE:
    # define the many-to-many table
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
    )
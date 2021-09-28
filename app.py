from flask import Flask, jsonify

import numpy as np

import pandas as pd

import datetime as dt

import sqlalchemy

from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import Session

from sqlalchemy import create_engine, func, inspect

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.measurement

pyapp = flask(app)

def home():

def precipitation(): 
    session = Session(engine)

    most_recent = session.query(func.max(measurement.date)).all()
    rain = dt.datetime(2017, 8, 23)
    year = rain - dt.timedelta(days=365)
    precip = session.query(measurement.date, measurement.prcp)

    def stations():
        session = Session(engine)
        stations = session.query(station.station).group_by(station.station).nunique()
        session.query(station.station, func.count(station.id)).group_by(station.station).order_by(func.count(station.id).desc()).all()
        active = session.query(station.station, func.count(station.id))[0]
    active.meaurement.tobs.max()
    active.measurement.tobs.min()
    active.measurement.tobs.mean()
    return jsonify(stations)

    def tobs():
        session = Session(engine)
         most_recent = session.query(func.max(measurement.date)).all()
         rain = dt.datetime(2017, 8, 23)
        year = rain - dt.timedelta(days=365)
        temperature = session.query(measurement.tobs)
        temp2 = [{'Temperature': result[0]} for result in temperature]
        return jsonify(temperature)








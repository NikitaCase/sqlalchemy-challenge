# import pandas resources 
import pandas as pd
import datetime as dt  


# import sqlalchemy resources 
import sqlalchemy
from sqlalchemy import create_engine, func 
from sqlalchemy.orm import Session 
from sqlalchemy.ext.automap import automap_base

# import flask
from flask import Flask, jsonify 

#-------------------------------------------------------------------------------------
 
#Database Setup 
engine = create_engine('sqlite:///C:/Users/guyan/Desktop/git desktop/sqlalchemy-challenge/Resources/hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)

print(Base.classes.keys()) 

#reflect tables
measurement = Base.classes.measurement
station = Base.classes.station 

#------------------------------------------------------------------------------------

#Flask setup 
app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return (
        f"Welcome to the Hawaii Weather Data API</br>"
        f"Available Routes:</br>"
        f"/api/v1.0/precipitaton</br>"
        f"/api/v1.0/stations -- Returns a JSON list of stations from the dataset </br>"
        f"/api/v1.0/tobs</br>"
        )

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    station_list = session.query(station.station).all()
    session.close()
    return jsonify(station_list)
    

@app.route('/api/v1.0/precipitation')
def prcp():
    session = Session(engine)
    yr_ago = dt.date(2016, 8, 23)
    precip = session.query(measurement.date, measurement.prcp)\
        .filter(measurement.date > yr_ago).all()
    session.close()

    prcp_list =[]
    for date, prcp in precip:
        prcp_dict ={}
        prcp_dict['date'] = date 
        prcp_dict['prcp'] = prcp 
        prcp_list.append(prcp_dict)
    return jsonify(prcp_list)


'''


@app.route('/api/v1.0/tobs')
def tobs:



   
'''










if __name__ == '__main__': 
    app.run(debug=True)
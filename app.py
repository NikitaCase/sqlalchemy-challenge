# import pandas resources 
import pandas as pd
import datetime as dt  
from datetime import date


# import sqlalchemy resources 
import sqlalchemy
from sqlalchemy import create_engine, func 
from sqlalchemy.orm import Session 
from sqlalchemy.ext.automap import automap_base

# import flask
from flask import Flask, jsonify 

#-------------------------------------------------------------------------------------
 
#Database Setup 
engine = create_engine('sqlite:///Resources/hawaii.sqlite')
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
        f"Welcome to the Hawaii Weather Data API</br></br>"
        f"Available Routes:</br>----------------------</br></br>"
        f"/api/v1.0/stations</br>Returns a JSON dictionary of stations from the dataset</br></br>"
        f"/api/v1.0/precipitaton</br>Returns JSON dictionary of dates and precipation recorded for the final year </br></br>"
        f"/api/v1.0/tobs</br>Returns dates and temperature observations of the most active station for the last year of data</br></br>"
        f"/api/v1.0/(start date)</br>\
            Accepts a start date in the form yyyy-mm-dd and finds minimum, maximum and average temperatures for the period starting from your input date to the end of the dataset 2017-08-22</br></br>"
        f"/api/v1.0/(start date)/(end date)</br>\
            Accepts start & end dates in the form yyyy-mm-dd and finds minimum, maximum and average temperatures for dates between the start and end date inclusive</br></br>"
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


@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    yr_ago = dt.date(2016, 8, 23)
    station_activity = session.query(measurement.station, func.count(measurement.station))\
        .group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
    active_station = station_activity[0][0] 
    temp = session.query(measurement.date, measurement.tobs)\
        .filter(measurement.station == active_station)\
            .filter(measurement.date > yr_ago).all()
    session.close()

    return jsonify(temp)


@app.route ('/api/v1.0/<start>')
def tempfrom(start):
    session = Session(engine)

    start_date = date(*map(int, start.split('-')))

    temps = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs))\
        .filter(measurement.date >= start_date).all()
    session.close()

    temp_list =[]
    for temp in temps:
        temp_dict ={}
        temp_dict['Minimum Recorded Temperature'] = temps[0][0]
        temp_dict['Maximum Recorded Temperature'] = temps[0][1]
        temp_dict['Average Recorded Temperature'] = temps[0][2]
        temp_list.append(temp_dict)

    return jsonify(temp_list)


@app.route ('/api/v1.0/<start>/<end>')
def tempfromto(start,end):
    session = Session(engine)

    start_date = date(*map(int, start.split('-')))
    end_date = date(*map(int, end.split('-')))

    temps = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs))\
        .filter(measurement.date >= start_date).filter(measurement.date <= end_date).all()
    session.close()

    temp_list =[]
    for temp in temps:
        temp_dict ={}
        temp_dict['Minimum Recorded Temperature'] = temps[0][0]
        temp_dict['Maximum Recorded Temperature'] = temps[0][1]
        temp_dict['Average Recorded Temperature'] = temps[0][2]
        temp_list.append(temp_dict)

    return jsonify(temp_list)




if __name__ == '__main__': 
    app.run(debug=True)
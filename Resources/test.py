# import panda resources 
import pandas as pd
import numpy as np
import datetime as dt  
import matplotlib.pyplot as plt

# import sqlalchemy resources 

import sqlalchemy
from sqlalchemy import create_engine, func 
from sqlalchemy.orm import Session 
from sqlalchemy.ext.automap import automap_base

# import flask
from flask import Flask, jsonify 

 
#sqlalchemy setup 
engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)

print(Base.classes.keys()) #testing the above to see if it works 
#!!!YAAAASSSS we may continue 

#reflect tables
measurement = Base.classes.measurement
station = Base.classes.station 

#Flask setup 
app = Flask(__name__)

@app.route('/')
def home():
    return('available api routes')
    return('')

@app.route('/api/v1.0/precipitation')
def prcp():


# if __name__ == '__main__': 
 #   app.run(debug=True)


'''
/api/v1.0/precipitation


Convert the query results to a dictionary using date as the key and prcp as the value.


Return the JSON representation of your dictionary.




/api/v1.0/stations

Return a JSON list of stations from the dataset.



/api/v1.0/tobs


Query the dates and temperature observations of the most active station for the last year of data.


Return a JSON list of temperature observations (TOBS) for the previous year.




/api/v1.0/<start> and /api/v1.0/<start>/<end>


Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.


When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.


When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.





Hints


You will need to join the station and measurement tables for some of the queries.


Use Flask jsonify to convert your API data into a valid JSON response object.




Bonus: Other Recommended Analyses

The following are optional challenge queries. These are highly recommended to attempt, but not required for the homework.


Temperature Analysis I


Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?


You may either use SQLAlchemy or pandas's read_csv() to perform this portion.


Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.


Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?



Temperature Analysis II


The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.


Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").


Plot the min, avg, and max temperature from your previous query as a bar chart.


Use the average temperature as the bar height.


Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).






Daily Rainfall Average


Calculate the rainfall per weather station using the previous year's matching dates.


Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.


You are provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic TOBS that match that date string.


Create a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.


Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.


Use Pandas to plot an area plot (stacked=False) for the daily normals.
'''




##############################################
# Team Activity 12, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################

import pandas



data = pandas.read_csv("weather_year.csv")

#print(data["EDT"])

#print(data[["EDT", "Mean TemperatureF"]])

#print(data.EDT)

#print(data.EDT.head())

data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

#print(data)

#print(data.mean_temp.std())

print(data.mean_temp.plot())



#print(data.std())

#first_date = data.date.values[0]
#print(first_date)

#from datetime import datetime
#datetime.strptime(first_date, "%Y-%m-%d")


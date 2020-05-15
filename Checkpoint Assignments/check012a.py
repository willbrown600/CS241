##############################################
# Checkpoint 012a, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
#
##############################################

import pandas

csv_data = pandas.read_csv("weather.csv")

median = csv_data.median()

print(median[0])




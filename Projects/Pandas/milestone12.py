##############################################
# Milestone Assignment 12, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
#
##############################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.chdir("/Users/William/Documents/BYUI Idaho/CS241/Pandas/nba_basketball_data/")

players_data = pd.read_csv("basketball_players.csv")

"""Some players score a lot of points because they attempt a lot of shots.
Among players that have scored a lot of points, are there some that are much more
efficient (points per attempt) than others? """

#free goal success
"""players_data["fgSuccess"] = (players_data["fgMade"] / players_data["fgAttempted"]) * 100

#print(players_data["fgSuccess"])
players_data = players_data[(players_data.fgAttempted > 0)]
players_data = players_data[(players_data.fgMade < players_data.fgAttempted)]

print(players_data[["fgSuccess", "playerID"]].sort_values("fgSuccess", ascending=False).head(10))



#Free throw percentages
players_data["ftSuccess"] = (players_data["ftMade"] / players_data["ftAttempted"]) * 100

#print(players_data["ftSuccess"])
players_data = players_data[(players_data.ftAttempted > 0)]
players_data = players_data[(players_data.ftMade < players_data.ftAttempted)]

print(players_data[["ftSuccess", "playerID"]].sort_values("ftSuccess", ascending=False).head(10))



#Three Pointer

players_data["threeSuccess"] = (players_data["threeMade"] / players_data["threeAttempted"]) * 100

players_data = players_data[(players_data.threeAttempted > 0)]
players_data = players_data[(players_data.threeMade < players_data.threeAttempted)]

print(players_data[["threeSuccess", "playerID"]].sort_values("threeSuccess", ascending=False).head(10))

master = pd.read_csv("basketball_master.csv")

nba = pd.merge(players_data, master, how="left", left_on="playerID", right_on="bioID")

print(nba[["useFirst", "lastName", "tmID", "fgSuccess"]].sort_values("fgSuccess", ascending=False).head(10))"""

"""It seems like some players may excel in one statistical category, but produce very little in other areas.
Are there any players that are exceptional across many categories? """

print(players_data.columns)


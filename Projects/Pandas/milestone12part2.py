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
players_data["fgSuccess"] = (players_data["fgMade"] / players_data["fgAttempted"]) * 100

#print(players_data["fgSuccess"])
players_data = players_data[(players_data.fgAttempted > 0)]
players_data = players_data[(players_data.fgMade < players_data.fgAttempted)]

print(players_data[["fgSuccess", "playerID"]].sort_values("fgSuccess", ascending=False).head(10))


#Free throw Success
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






"""It seems like some players may excel in one statistical category, but produce very little in other areas.
Are there any players that are exceptional across many categories? """

#Max number of points scored by player over season.
data = players_data[(players_data.points > 200)]
data = players_data[(players_data.assists > 30)]
data = players_data[(players_data.rebounds > 15)]
#Max number of points scored, assists, steals and rebounds by player per year 

print(data[["playerID", "points", "assists", "rebounds"]].sort_values("points", ascending=False).head(10))





"""Much has been said about the rise of the three-point shot in recent years.
It seems that players are shooting and making more three-point shots than ever.
Recognizing that this dataset doesn't contain the very most recent data,
do you see a trend of more three-point shots either across the league or among certain groups of players?
Is there a point at which popularity increased dramatically?"""

master = pd.read_csv("basketball_master.csv")

nba = pd.merge(players_data, master, how="left", left_on="playerID", right_on="bioID")

nba_grouped_year = nba[["threeAttempted", "year"]].groupby("year").median()

nba_grouped_year = nba_grouped_year.reset_index()
print(nba_grouped_year)

sns.barplot(data=nba_grouped_year, x="year", y="threeAttempted").set_title("Attempted Three pointers per year")

plt.show()
plt.savefig("regplot_medianThreePointers_per_year.png")

"""I think it was about 1988 where significant numbers of attempted three pointers increased and began to start a
trend change."""

"""Many sports analysts argue about which player is the GOAT (the Greatest Of All Time).
Based on this data, who would you say is the GOAT? Provide evidence to back up your decision.
"""
greats = pd.read_csv("basketball_player_allstar.csv")

print(greats.columns)

greatest = pd.merge(greats, master, how= "left", left_on="player_id", right_on="bioID")

print(greatest[["player_id", "points", "rebounds", "assists", "steals"]].sort_values("points", ascending=False).head(10))


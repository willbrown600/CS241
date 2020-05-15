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

#print(players_data)

print(players_data.columns)

players_median = players_data.points.median()

players_mean = players_data.points.mean()

players_max = players_data.points.max()

print("Median: ")
print(players_median)
print("Mean: ")
print(players_mean)
print("Max: ")
print(players_max)

"""Determine the highest number of points recorded in a single season.
Identify who scored those points and the year they did so."""

print(players_data[["playerID","year","points"]].sort_values("points",ascending=False))

master = pd.read_csv("basketball_master.csv")

nba = pd.merge(players_data, master, how="left", left_on="playerID", right_on="bioID")

#print(nba.columns)

print(nba[["year", "useFirst", "lastName", "tmID", "points"]].sort_values("points", ascending=False).head(10))

"""Produce a boxplot that shows the distribution of total points, total assists,
and total rebounds (each of these three is a separate box plot,
but they can be on the same scale and in the same graphic).   """

sns.boxplot(data=nba[["points", "assists", "rebounds"]])

plt.show()

plt.savefig("boxplot_distribution.png")

"""Produce a plot that shows how the number of points scored has changed over time
by showing the median of points scored per year, over time.
The x-axis is the year and the y-axis is the median number of points among all players for that year. """

nba_grouped_year = nba[["points", "year"]].groupby("year").median()
#print(nba_grouped_year)

nba_grouped_year = nba_grouped_year.reset_index()
print(nba_grouped_year)

sns.regplot(data=nba_grouped_year, x="year", y="points").set_title("Median points per year")


plt.show()
plt.savefig("regplot_medianPoints_per_year.png")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def get_crash_data():
	daily_crashes = pd.read_csv("nyc_crash_data/daily_crash_data.csv")
	daily_crashes.crash_date = pd.to_datetime(daily_crashes.crash_date)

	# Only include 2015 - 2019 crash data
	daily_crashes = daily_crashes[daily_crashes["crash_date"] >= '2015-01-01']
	daily_crashes = daily_crashes[daily_crashes["crash_date"] <= '2019-12-31']
	return daily_crashes

# Crashes by Day, pretty noisey
def plot_crashes_by_day():
	daily_crashes.plot(x='crash_date', y='crashes',linewidth=0.5)
	plt.show()

# Injuries by Day, pretty noisey
def plot_injuries_by_day():
	daily_crashes.plot(x='crash_date', y='injuries',linewidth=0.5)
	plt.show()

def injuries_by_week_of_year():
	weekly_crashes = daily_crashes.groupby(by=["crash_year", "crash_woy"]).sum()
	weekly_crashes.unstack("crash_year").plot(y='injuries')
	plt.show()
# weekly_crashes.plot(x='crash_woy', y='crashes',linewidth=0.5)
# plt.show()

if __name__ == "__main__":
	daily_crashes = get_crash_data()
	plot_crashes_by_day()
	plot_injuries_by_day()
	injuries_by_week_of_year()

	# daily_crashes['dow'] = daily_crashes['crash_date'].dt.weekday
	# print(daily_crashes)

	# # print(daily_crashes['crash_date'].dt.weekday)
	# daily_crashes['crash_week_start'] = daily_crashes['crash_date'] - pd.timedelta(days=daily_crashes['dow'])
	# print(daily_crashes)
	# plot_injuries_by_day()
	# crashes_by_week_of_year()
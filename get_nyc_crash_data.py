import pandas as pd
from sodapy import Socrata
import secrets


my_app_token = secrets.my_app_token
username = secrets.username
password = secrets.password

# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofnewyork.us",
                 my_app_token,
                 username=username,
                 password=password)

# # Day-level aggregation of NYC crashes, injuries, and deaths
# daily_crashes = client.get("h9gi-nx95",
# 						 select="crash_date, \
# 						 	date_extract_y(crash_date) AS crash_year, \
# 						 	date_extract_m(crash_date) AS crash_month, \
# 						 	date_extract_woy(crash_date) AS crash_woy, \
# 						 	COUNT(crash_date) as crashes, \
# 						 	SUM(number_of_persons_injured) AS injuries, \
# 						 	SUM(number_of_persons_killed) AS deaths",
# 						 group="crash_date",
# 						 # where="crash_date >= 2015-01-01T00:00:00.000",
# 						 order="crash_date ASC",
# 						 limit=5000)

# daily_crash_df = pd.DataFrame.from_records(daily_crashes)
# daily_crash_df.to_csv("nyc_crash_data/daily_crash_data.csv", index=False)

# Week-level aggregation of NYC crashes, injuries, and deaths
weekly_crashes = client.get("h9gi-nx95",
						 select=" \
						 	date_extract_woy(crash_date) AS crash_woy, \
						 	date_extract_y(crash_date) AS crash_year, \
						 	date_extract_m(crash_date) AS crash_month, \
						 	MIN(crash_date) AS crash_week_start, \
						 	COUNT(crash_date) as crashes, \
						 	SUM(number_of_persons_injured) AS injuries, \
						 	SUM(number_of_persons_killed) AS deaths",
						 group="crash_woy, crash_year",
						 # where="crash_date >= 2015-01-01T00:00:00.000",
						 order="crash_date ASC",
						 limit=5000)

print(weekly_crash_df)

weekly_crash_df = pd.DataFrame.from_records(weekly_crashes)
weekly_crash_df.to_csv("nyc_crash_data/weekly_crash_data.csv", index=False)

client.close()
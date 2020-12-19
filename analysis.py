import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

daily_crashes = pd.read_csv("nyc_crash_data/daily_crash_data.csv")

daily_crashes.crash_date = pd.to_datetime(daily_crashes.crash_date)
daily_crashes = daily_crashes.set_index('crash_date')

daily_crashes['crashes'].plot(linewidth=0.5)
plt.show()


# print(daily_crashes.dtypes)
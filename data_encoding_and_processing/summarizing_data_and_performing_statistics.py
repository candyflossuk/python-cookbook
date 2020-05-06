"""
This script shows how to crunch through large datasets and generate summaries 
or other kinds of stats

For anything involving stats, time series ore related use Pandas.

This example uses the rat and rodent database of chicago see:
https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Rodent-Baiting-Historical/97t6-zrhs
"""
import pandas

rats = pandas.read_csv("rats.csv", skip_footer=1)

# Range of values for a certain field
rats["Current Activity"].unique()

# Filter data
crew_dispatched = rats[rats["Current Activity"] == "Dispatch Crew"]
len(crew_dispatched)

# Find 10 most rat infested ZIP codes in Chicago
crew_dispatched["ZIP Code"].value_counts()[:10]

# Group by completion date
dates = crew_dispatched.groupby("Completion Date")
len(dates)

# Determine counts on each day
date_counts = dates.size()
date_counts[0:10]

# Sort the counts
date_counts.sort()
date_counts[-10:]

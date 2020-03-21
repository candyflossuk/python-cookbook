"""
This script shows how to loop over each date in the current month, and
how to calculate the date range

Calculate start and stop date then use datetime.timedelta objects to increment
the date as you go.

The following function takes any datetime object, returns tuple containing first
date of the month and starting date of the next month
"""
from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date

# Loop over date range
a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day

# basic info for a calendar can be found using calendar module

# Below is a function that works like built-in range() function but for dates
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

# usage
for d in date_range(datetime(2012, 9, 1), datetime(2012,10,1), timedelta(hours=6)):
    print(d)

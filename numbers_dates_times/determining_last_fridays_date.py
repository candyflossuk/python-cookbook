"""
This script shows a general solution for finding a date for the last
occurrence of a day of the week - like last friday
"""
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def  get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

# within the interpreter
datetime.today() # for reference
get_previous_byday('Monday')
get_previous_byday('Tuesday')
get_previous_byday('Friday')

# optional start_date
get_previous_byday('Sunday', datetime(2012, 12, 21))
# datetime.datetime(2012, 12, 16, 0, 0)

"""
If you are doing lots of calculations like this - use python-dateutil package.
"""
d = datetime.now()
print(d + relativedelta(weekday=FR))  # Next friday
print(d + relativedelta(weekday=FR(-1)))  # Last friday

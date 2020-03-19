"""
This script shows how to do simple conversions like day to seconds, hours to minutes etc

use the datetime module
"""
from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
c.days  # 2
c. seconds  # 37800
c.seconds / 3600  # 10.5
c.total_seconds() / 3600  # 58.5

# To represent specific dates and times create datetime instances and use the standard mathematical operations to manipulate them
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))  # 2012-10-03 00:00:00
b = datetime(2012, 12, 21)
d = b-a
d.days  # 89
now = datetime.today()  # datetime.datetime(2020, 3, 19, 8, 57, 57, 398356)
print (now + timedelta(minutes=10))  # 2020-03-19 09:07:57.398356

# When making calculations - datetime is aware of leap years
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
a - b  # datetime.timedelta(days=2)
(a - b).days  # 2
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
(c - d).days

"""
For complex data manipulations - such as time zones, fuzzy time ranges, dates of holdays look at dateutil module.

-- pip install python-dateutil

dateutil.relativedelta() - fills in gaps pertaining to
handling of months (and differing number of days)
"""
a = datetime(2012, 9, 23)
a + timedelta(months = 1)  # TypeError: 'months' is an invalid keyword argument for __new__()

a + relativedelta(months=+1)
a + relativedelta(months=+4)

# Time between two dates
b = datetime(2012, 12, 21)
d = b - a  # datetime.timedelta(days=89)
d = relativedelta(b, a)  # relativedelta(months=+2, days=+28)
relativedelta(months=+2, days=+28)
d.months  # 2
d.days  # 28



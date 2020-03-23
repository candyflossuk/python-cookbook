"""
This script shows how to manipulate dates involving time zones.

For most problems involving time zones - use the pytz module.
The pytz module provides the Olson time zone database - which is the defacto
for most OS' and languages.

A major use is localizing simple dates created with datetime
"""
from datetime import datetime
import pytz
from pytz import timezone
from datetime import timedelta

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)  # 2012-12-21 09:30:00

# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)  # 2012-12-21 09:30:00-06:00

"""
Once localized it can be convered to other time zones
"""
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)  # 2012-12-21 21:00:00+05:30

"""
When performing arithmetic with localized dates - you must take daylight 
savings into account. For example the following is WRONG
"""
d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)  # 2013-03-10 01:45:00-06:00

later = loc_d + timedelta(minutes=30)
print(later)  # 2013-03-10 02:15:00-06:00  # WRONG!

# Wrong because it does not account for the one-hour skip in local time - to fix use normalize()
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)  # 2013-03-10 03:15:00-05:00

"""
To stop you going mad - a common strategy is to convert all dates to UTC and use that for internal storage 
and manipulation...
"""
utc_d = loc_d.astimezone(pytz.utc)  # 2013-03-10 07:45:00+00:00
# To then convert to the local time later
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))  # 2013-03-10 03:15:00-05:00

"""
Figuring out the time zones to use is also tricky
To find this out consult the pytz.country_time-zones dictionary
"""
pytz.country_timezones('IN')

# SEE PEP-431 for more details on time zone support


"""
This script shows how to convert strings to datetime objects
to perform non string operations on them
"""

from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')  # Performance is not great - as deals with system locale settings
z = datetime.now()
diff = z - y
diff  # datetime.timedelta(days=2740, seconds=35151, microseconds=478178)

# datetime -> string object can also be formatted using datetime.strftime
nice_z = datetime.strftime(z, '%A %B %d, %Y')
nice_z  # 'Sunday March 22, 2020'

# If doing lots of formatting and you know the formatt roll your own


def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

# This will be a lot faster than datetime.strptime().

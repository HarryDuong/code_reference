"""
This contains pieces of codes that I collect overtime to make code more efficient.
"""

# ─── DISTINGUISHING MULTIPLE EXIT POINT ─────────────────────────────────────────
from datetime import datetime, timezone, timedelta
from dateutil import tz
from datetime import datetime
from collections import defaultdict


def find(seq, target):
    """
    This to demonstrate the 'else' function in a for loop. 
    Using 'else' in for loop to do an action if there was
    no break found in the loop.

    """
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1

    return i


# ─── LOOPING OVER DICTIONARY KEYS AND DELETE KEYS WITH CRITERIA ─────────────────
d = {'a': 1, 'a3': 3, 'b': 4}

# instead of looping over each keys and delete items
d = {k: d[k] for k in d if not k.startswith('r')}

# ─── COUNTING WITH DICSTIONARY ──────────────────────────────────────────────────

colors = ['red', 'green', 'blue', 'blue', 'red', 'red']
# noinspection PyRedeclaration
d = dict()

# First method
for color in colors:
    d[color] = d.get(color, 0) + 1

# Using default dict:
d = defaultdict(int)

for color in colors:
    d[color] += 1  # If color is not exists yet,

# ─── GROUPING WITH DICTIONARY ───────────────────────────────────────────────────

# Following code using default dict to group items together base on key.
# keys can be defined by any critera.
colors = ['red', 'green', 'blue', 'blue', 'red', 'red']
d = defaultdict(list)
for color in colors:
    key = len(color)
    d[key].append(color)

# ─── DICTIONARY POPITEM ─────────────────────────────────────────────────────────

# returns an arbitrary element (key, value) pair from the dictionary
# removes an arbitrary element (the same element which is returned) from the dictionary.

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

result = person.popitem()
print('person = ', person)
print('Return Value = ', result)

# Below is the result, the last item ('salary':3500.0) is
# removed first from the dictionary and assigned to result.
# The original dictionary only have 2 items remain.

# person =  {'name': 'Phill', 'age': 22}
# Return Value =  ('salary', 3500.0)


# ─── CONVERT TIMESTAMP FROM UTC TO OTHER TIMEZONE  ─────────────────────────────────────────────────────────
from datetime import datetime


def convert_time_from_utc(timestamp, to_time_zone = 'Australia/Melbourne', output_format = None):
    """
    Convert utc timestamp to other timestamp

    Args:
        timestamp: datetime object or string present datetime.
                    if the input is string it must follow 'YYYY-MM-DD HH:MM:SS'

        to_time_zone: to the desire timezone
        output_format: 'datetime' or string format of time
                    If set as None, then function return exactly the same type as input.

    Returns:
        datetime object or string presenting datetime in new time zone
    """

    if output_format is None:
        if type(timestamp) is str:
            output_format = 'str'
            timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        elif (type(timestamp) is datetime) or (type(timestamp) is datetime):
            output_format = 'datetime'
        else:
            raise ValueError(
                    'input timestamp must either string YYYY-MM-DD HH:MM:SS or a datetime object')

    utc_tz = tz.gettz('UTC')
    to_tz = tz.gettz(to_time_zone)

    output = timestamp.replace(tzinfo = utc_tz)
    output = output.astimezone(to_tz)

    if output_format == 'datetime':
        return output
    elif output_format == 'str':
        return datetime.strftime(output, '%Y-%m-%d %H:%M:%S')
    else:
        return datetime.strftime(output, output_format)


# ─── GET EPOCH ──────────────────────────────────────────────────────────────────

import time

time.time()  # ==> give epoch number of seconds from 1 Jan 1970

datetime.fromtimestamp(time.time())  # ==> get timestamp from

# ─── GET TODAY DATE IN UTC TIME ZONE ────────────────────────────────────────────

# today date at utc:
datetime.now(timezone.utc)

# 5 days before current time:
datetime.today() + timedelta(days = -5)

# ─── DOWNLOAD NO TEXT DATA FROM WEB ─────────────────────────────────────────────
# when download image file from web and write it to disk using open method. 
# There are cases that the image data is broken. Below code at least will warn us 
# if the image file is broken

import requests
from PIL import Image
from io import BytesIO

# noinspection PyUnresolvedReferences
r = requests.get(url)
i = Image.open(BytesIO(r.content))
i.save('file_name.jpg')

# ------------------------------------------------------------------------------
def parse_http_retry_after(hd):
    """
    Parse a HTTP Retry-After response header
    Return number of seconds to wait. Default to 15 if Retry-Header doesn't
    exist or isn't integer number of seconds or (limited type) parsable date
    :param hd:  Headers from a http response (requests version)
    :type hd:   dict
    :return:        Number of seconds to wait
    :rtype:         int
    """
    retry_time = 15
    try:
        retry_time = hd['Retry-After']
        try:
            retry_time = int(hd['Retry-After']) + 10
            return retry_time
        except ValueError:
            pass
        retry_time = datetime_val(retry_time)
        retry_time = (retry_time - datetime_with_utc_tz()).total_seconds()
        retry_time = round(retry_time) + 10
    except KeyError:
        pass
    return retry_time


def datetime_val(tv):
    """
    Uses dateutil parser. Set UTC for datetime without tzinfo
    :param tv:  date
    :type  tv:  str
    :return:    datetime parsed result
    :rtype:     datetime.datetime
    """
    tv = dateutil.parser.parse(tv)
    if tv.tzinfo is None:
        tv = tv.replace(tzinfo = dateutil.tz.UTC)
    return tv


def datetime_with_utc_tz():
    """
    Return the UTC time datetime set timezone UTC
    To convert to a particular TZ use r_date.astimezone(dateutil.tz.gettz("Australia/Melbourne"))
    or as offset time r_date.astimezone(dateutil.tz.tzstr("GMT+11:00", posix_offset=False))
    :return:    current date and time with UTC timezone
    :rtype:     datetime.datetime
    """
    return datetime.datetime.utcnow().replace(tzinfo = dateutil.tz.UTC)


# ------------------------------------------------------------------------------
# To get logger name
PROG = os.path.splitext(os.path.basename(sys.argv[0]))[0]
LOG = logging.getLogger(name = PROG)

# ─── DISTINGUISHING MULTIPLE EXIT POINT ─────────────────────────────────────────
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
d = {}

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
from dateutil import tz

def convert_time_from_utc(timestamp, to_time_zone = 'Australia/Melbourne'):
    """
    Convert utc timestamp to other timestamp

    Args:
        timestamp: datetime object or string present datetime.
                    if the input is string it must follow 'YYYY-MM-DD HH:MM:SS'
        to_time_zone: to the desire timezone

    Returns:
        datetime object or string presenting datetime in new time zone
    """

    if type(timestamp) is str:
        input_type = 'str'
        timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    elif (type(timestamp) is datetime) or (type(timestamp) is datetime.datetime):
        input_type = 'datetime'
    else:
        raise ValueError('input timestamp must either string YYYY-MM-DD HH:MM:SS or a datetime object')

    utc_tz = tz.gettz('UTC')
    to_tz = tz.gettz(to_time_zone)

    output = timestamp.replace(tzinfo = utc_tz)
    output = output.astimezone(to_tz)

    if input_type == 'str':
        output = datetime.strftime(output, '%Y-%m-%dT%H:%M:%SZ')

    return output

#
# ──────────────────────────────────────────────────────────────────────────────────
#   :::::: P A N D A S   D A T A F R A M E : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────
#

# ─── DATAFRAME REPLACE ──────────────────────────────────────────────────────────

DataFrame.replace(to_replace=None, value=None, inplace=False,
                  limit=None, regex=False, method='pad')

# to_replace : str, regex, list, dict, Series, int, float, or None

# Using a list of dictionary for multiple replacment
df.replace({'a': 1, 'b': 2, 'c:3'}, inplace=True)

# Using Regex for newline cleanup



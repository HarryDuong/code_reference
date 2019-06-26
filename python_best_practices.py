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



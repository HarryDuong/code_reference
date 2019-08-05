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


def convert_time_from_utc(timestamp, to_time_zone='Australia/Melbourne', output_format=None):
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
        elif (type(timestamp) is datetime) or (type(timestamp) is datetime.datetime):
            output_format = 'datetime'
        else:
            raise ValueError(
                'input timestamp must either string YYYY-MM-DD HH:MM:SS or a datetime object')

    utc_tz = tz.gettz('UTC')
    to_tz = tz.gettz(to_time_zone)

    output = timestamp.replace(tzinfo=utc_tz)
    output = output.astimezone(to_tz)

    if output_format == 'datetime':
        return output
    elif output_format == 'str':
        return datetime.strftime(output, '%Y-%m-%d %H:%M:%S')
    else:
        return datetime.strftime(output, output_format)


# ─── GET TODAY DATE IN UTC TIME ZONE ─────────────────────────────────────────────────────────

# today date at utc:
datetime.now(timezone.utc)

# 5 days before current time:
datetime.today() + timedelta(days=-5)

# ─── DOWNLOAD NO TEXT DATA FROM WEB ─────────────────────────────────────────────
# when download image file from web and write it to disk using open method. 
# There are cases that the image data is broken. Below code at least will warn us 
# if the image file is broken

import requests
from PIL import Image
from io import BytesIO
r = requests.get(url)
i = Image.open(BytesIO(r.content))
i.save('file_name.jpg')

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

# ─── FIND A LIST OF DUPLICATED COLUMN NAME IN MULTIPLE DATA FRAME ───────────────

all_columns = pd.Series(list(df1) + list(df2))
all_columns[all_columns.duplicated()]

# Note that list(df) give a list of column in a dataframe

# ─── EXTRACT PHONE NUMBER ───────────────────────────────────────────────────────
# Using str.extract function in pandas dataframe to apply regex pattern on 
# a column and return a new column

# Series.str.extract(pat, flags=0, expand=True)
# Extract capture groups in the regex pat as columns in a DataFrame.

# https://stackoverflow.com/a/16699507/3331408
phone_pattern = r'((\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4})'
patients_clean['phone_number'] = patients_clean.contact.str.extract(phone_pattern)[0]

# ─── EXTRACT EMAIL ──────────────────────────────────────────────────────────────
# http://emailregex.com/
email_pattern = r"([a-zA-Z][a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
patients_clean['email'] = patients_clean.contact.str.extract(email_pattern)


# ─── RESHAPE DATA FROM WIDE TO LONG ─────────────────────────────────────────────
# https://deparkes.co.uk/2016/10/28/reshape-pandas-data-with-melt/

# pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, 
#               value_name='value', col_level=None)
# Unpivots a DataFrame from wide format to long format, 
# optionally leaving identifier variables set.

>>> df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
...                    'B': {0: 1, 1: 3, 2: 5},
...                    'C': {0: 2, 1: 4, 2: 6}})
>>> df
   A  B  C
0  a  1  2
1  b  3  4
2  c  5  6
>>> pd.melt(df, id_vars=['A'], value_vars=['B', 'C'])
   A variable  value
0  a        B      1
1  b        B      3
2  c        B      5
3  a        C      2
4  b        C      4
5  c        C      6

# ─── NUMPY ──────────────────────────────────────────────────────────────────────

import numpy as np

a = np.arange(0,36)

array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35])

a = a.reshape(6,6)
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35]])

a = a.reshape(36)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35])

a.reshape(36)[::7] # note the [::7], it steps every 7th elements
array([ 0,  7, 14, 21, 28, 35])
# https://docs.python.org/2.3/whatsnew/section-slices.html



# ─── BARCHART WITH SEABORN ──────────────────────────────────────────────────────

import seaborn as sns

sns.countplot(data= df, x = 'col_name')     

# Select a color for barchart
base_color = sns.color_palette()[0]
sns.countplot(data = df, x = 'cat_var', color = base_color)


#           .                                                             .      
#       /*/ .                                ############.                .      
#           . ............                   ############.                .      
#           . ((((((((((((.                  ############.                .      
#        .. . ((((((((((((.                  ############.                .      
#           . ((((((((((((.                  ############.                .      
#           . ((((((((((((.                  ############.                .      
#           . ((((((((((((.                  ############.  /(((((((((((( .      
#        *  . ((((((((((((.                  ############.  /(((((((((((( .      
#    ,,     . ((((((((((((.                  ############.  /(((((((((((( .      
#    **     . ((((((((((((.   ************   ############.  /(((((((((((( .      
#           . ((((((((((((.  .////////////   ############.  /(((((((((((( .      
#        /  ( ((((((((((((.  .////////////   ############.  /(((((((((((( .      
#           . ((((((((((((.  .////////////   ############.  /(((((((((((( .      
#           . ((((((((((((.  .////////////   ############.  /(((((((((((( .      
#           . ((((((((((((.  .////////////   ############.  /(((((((((((( .      
#        ,. . ((((((((((((.  .////////////   ############.  /(((((((((((( .      
#           . ((((((((((((.  .////////////   ############.  /(((((((((((( .      
#           . ((((((((((((.  .////////////   ############.  /(((((((((((( .      
#         / . ((((((((((((.  .////////////   ############.  /(((((((((((( .      
#                /               /. .            /               * .             

# Sort bar chart:
base_color = sb.color_palette()[0]
cat_order = df['cat_var'].value_counts().index
sb.countplot(data = df, x = 'cat_var', color = base_color, order = cat_order)

#       /*/ . ((((((((((((.                                               .      
#           . ((((((((((((.   ............                                .      
#           . ((((((((((((.  .((((((((((((                                .      
#        .. . ((((((((((((.  .((((((((((((                                .      
#           . ((((((((((((.  .((((((((((((                                .      
#           . ((((((((((((.  .((((((((((((                                .      
#           . ((((((((((((.  .((((((((((((   ((((((((((((.                .      
#        *  . ((((((((((((.  .((((((((((((   ((((((((((((.                .      
#    ,,     . ((((((((((((.  .((((((((((((   ((((((((((((.                .      
#    **     . ((((((((((((.  .((((((((((((   ((((((((((((.  *//////////// .      
#           . ((((((((((((.  .((((((((((((   ((((((((((((.  /(((((((((((( .      
#        /  ( ((((((((((((.  .((((((((((((   ((((((((((((.  /(((((((((((( .      
#           . ((((((((((((.  .((((((((((((   ((((((((((((.  /(((((((((((( .      
#           . ((((((((((((.  .((((((((((((   ((((((((((((.  /(((((((((((( .      
#           . ((((((((((((.  .((((((((((((   ((((((((((((.  /(((((((((((( .      
#        ,. . ((((((((((((.  .((((((((((((   ((((((((((((.  /(((((((((((( .      
#           . ((((((((((((.  .((((((((((((   ((((((((((((.  /(((((((((((( .      
#           . ((((((((((((.  .((((((((((((   ((((((((((((.  /(((((((((((( .      
#         / . ((((((((((((.  .((((((((((((   ((((((((((((.  /(((((((((((( .      
#                 / .           *                , ,            .. ,           

# For ordinal data type, we want to sort by the its order instead:

level_order = ['Alpha', 'Beta', 'Gamma', 'Delta']
ordered_cat = pd.api.types.CategoricalDtype(ordered = True, categories = level_order)
df['cat_var'] = df['cat_var'].astype(ordered_cat)

# # use this method if you have pandas v0.20.3 or earlier
# df['cat_var'] = df['cat_var'].astype('category', ordered = True,
#                                      categories = level_order)

base_color = sb.color_palette()[0]
sb.countplot(data = df, x = 'cat_var', color = base_color)

# ─── ROTATE AXIS TEXT ───────────────────────────────────────────────────────────

plt.xticks(rotation = 90)

# ─── RELATIVE FREQUENCY ─────────────────────────────────────────────────────────

# https://github.com/mwaskom/seaborn/issues/1027#issuecomment-250456545
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.DataFrame(dict(x=np.random.poisson(4, 500)))
ax = sns.barplot(x="x", y="x", data=df, estimator=lambda x: len(x) / len(df) * 100)
ax.set(ylabel="Percent")

# https://github.com/mwaskom/seaborn/issues/1027#issuecomment-360866896
df = sns.load_dataset("tips")
x, y, hue = "day", "prop", "sex"
hue_order = ["Male", "Female"]

f, axes = plt.subplots(1, 2)
sns.countplot(x=x, hue=hue, data=df, ax=axes[0])

prop_df = (df[x]
           .groupby(df[hue])
           .value_counts(normalize=True)
           .rename(y)
           .reset_index())

sns.barplot(x=x, y=y, hue=hue, data=prop_df, ax=axes[1])


# Stacked barchart with percentive
# https://github.com/mwaskom/seaborn/issues/1027#issuecomment-475091285
df = sns.load_dataset("tips")
props = df.groupby("day")['sex'].value_counts(normalize=True).unstack()
props.plot(kind='bar', stacked='True')


# Otherway to create relative frequency
# get proportion taken by most common group for derivation
# of tick marks
n_points = df.shape[0]
max_count = df['cat_var'].value_counts().max()
max_prop = max_count / n_points

# generate tick mark locations and names
tick_props = np.arange(0, max_prop, 0.05)
tick_names = ['{:0.2f}'.format(v) for v in tick_props]

# create the plot
base_color = sb.color_palette()[0]
sb.countplot(data = df, x = 'cat_var', color = base_color)
plt.yticks(tick_props * n_points, tick_names)
plt.ylabel('proportion')


# ─── ADD TEXT INSIDE BARCHART ───────────────────────────────────────────────────

# create the plot
base_color = sb.color_palette()[0]
sb.countplot(data = df, x = 'cat_var', color = base_color)

# add annotations
n_points = df.shape[0]
cat_counts = df['cat_var'].value_counts()
locs, labels = plt.xticks() # get the current tick locations and labels

# loop through each pair of locations and labels
for loc, label in zip(locs, labels):

    # get the text property for the label to get the correct count
    count = cat_counts[label.get_text()]
    pct_string = '{:0.1f}%'.format(100*count/n_points)

    # print the annotation just below the top of the bar
    plt.text(loc, count-8, pct_string, ha = 'center', color = 'w')

# ─── VISUALISE NAN VALUE ────────────────────────────────────────────────────────

na_counts = df.isna().sum()
base_color = sb.color_palette()[0]
sb.barplot(na_counts.index.values, na_counts, color = base_color)

# ─── PIE CHART ──────────────────────────────────────────────────────────────────
# https://academy.datawrapper.de/article/127-what-to-consider-when-creating-a-pie-chart
sorted_counts = df['cat_var'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False);
plt.axis('square')
# axis square to make sure it's circle

# ─── DONUT PLOT ─────────────────────────────────────────────────────────────────
# wedgeprops for the width of the hole in middle of pie chart
sorted_counts = df['cat_var'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False, wedgeprops = {'width' : 0.4});
plt.axis('square')

# ─── HISTORGRAM ─────────────────────────────────────────────────────────────────

plt.figure(figsize = [10, 5]) # larger figure size for subplots

# histogram on left, example of too-large bin size
plt.subplot(1, 2, 1) # 1 row, 2 cols, subplot 1
bin_edges = np.arange(0, df['num_var'].max()+4, 4)
plt.hist(data = df, x = 'num_var', bins = bin_edges)

# histogram on right, example of too-small bin size
plt.subplot(1, 2, 2) # 1 row, 2 cols, subplot 2
bin_edges = np.arange(0, df['num_var'].max()+1/4, 1/4)
plt.hist(data = df, x = 'num_var', bins = bin_edges)


# ─── KDE ────────────────────────────────────────────────────────────────────────

sb.distplot(df['num_var'])


bin_edges = np.arange(0, df['num_var'].max()+1, 1)
sb.distplot(df['num_var'], bins = bin_edges, kde = False,
            hist_kws = {'alpha' : 1})


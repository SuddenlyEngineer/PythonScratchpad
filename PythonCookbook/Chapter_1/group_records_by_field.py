from operator import itemgetter
from itertools import groupby
from collections import defaultdict

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# Sort by the desired field first
rows.sort(key=itemgetter('date'))

# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('    ', i) #The space is in there to make it look pretty

# groupby only examines consecutive items, so it must be sorted first
# To group the data together by dates into a random-access data structure, use defaultdict

rows_by_date = defaultdict(list) #Sorting isn't necessary, but this consumes more memory
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']: #Trades memory use for speed.
    print(r)
import csv
from collections import namedtuple
import re

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv: # Row will be a tuple. row[0] (Symbol) and row[4] (Change)
        # Process row 
        print('blah')

with open('stock.csv') as f: # namedtuples make life a lot easier. 
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r) # Unpack the CSV into namedtuples as described above.
        # Process row
    
# This allows row.Symbol and row.Change instead of indicies, that is, if column headers are valid Python identifiers.

# Can also read the data in as a sequence of dictionaries.

with open('stocks.csv') as f: 
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row
        print('blah')

# Can access the elements of each row using row headers, like row['Symbol'].

headers = ['Symbol','Price','Date','Time','Change','Volume'] # Now let's write CSV data.
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]

with open('stocks.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]

with open('stocks.csv','w') as f:
    f_csv = csv.DictWriter(f, headers) # If data, as above, in a sequence of dictionaries.
    f_csv.writeheader()
    f_csv.writerows(rows)

# By default, csv uses Microsoft Excel encoding rules, but there are tweaks available. 

with open('stock.tsv') as f:
    f_tsv = csv.reader(f, delimiter='\t') # Example of reading tab-separated values.
    for row in f_tsv:
        print('blah')

# Be careful validating column headers; use re to scrube headers to avoid namedtuple ValueErrors.
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headers = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv) ]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r) # Process row

# CSV does not interpret data and always returns strings. Fix this with: 
col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))

# Or with dictionaries: 
print('Reading as dicts with type conversion')
field_types = [ ('Price', float),
                ('Change', float),
                ('Volume', int) ]

with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)

# For more thorough analysis, use pandas.
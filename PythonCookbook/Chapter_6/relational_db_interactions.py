import sqlite3

stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]

db = sqlite3.connect('database.db') # Parameters like name of db, hostname, user/pass, etc.

c = db.cursor() # Needed for SQL queries
c.execute('create table portfolio (symbol text, shares integer, price real)')
db.commit()

c.executemany('insert into portfolio values (?,?,?)', stocks) # Insert a sequence of rows.
db.commit()

for row in db.execute('select * from portfolio'): # Perform a query
     print(row)

min_price = 100
for row in db.execute('select * from portfolio where price >= ?',(min_price,)): # To accept user-supplied input in queries, escape parameters using ?
    print(row)

# Never form SQL statement strings with % or .format because this opens the program to SQL-injection. ? is safe.
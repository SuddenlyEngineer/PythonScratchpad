######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])

'''Why do that, when you can do this?'''

SHARES = slice(20,32) #Creates a slice object usable anywhere a slice is allowed.
PRICE = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2,4)
assert items[2:4] == items[a]
items[a] = [10, 11]
print(items)
del items[a]
print(items)

a = slice(5, 50, 2)
a.start
a.stop
a.step

s = 'HelloWorld'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])
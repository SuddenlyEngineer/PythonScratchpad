print('ACME', 50, 91.5) # Returns ACME 50 91.5
print('ACME', 50, 91.5, sep=',') # Returns ACME,50,91.5
print('ACME', 50, 91.5, sep=',', end='!!\n') # Returns ACME,50,91.5!!

# You can also use end to suppress the output of newlines in output
for i in range(5):
    print(i, end=' ') # Returns 0 1 2 3 4

# You could use str.join, but it only works with strings
print(','.join('ACME','50','91.5'))

row = ('ACME', 50, 91.5)
print(','.join(str(x) for x in row)) # Returns ACME, 50, 91.5
print(*row, sep=',') # Much simpler way to do the same thing. 
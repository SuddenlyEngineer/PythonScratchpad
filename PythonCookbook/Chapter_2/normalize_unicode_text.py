import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalape\u0303o'
s1
s2
s1 == s2 # Asserts False
len(s1) # Returns 14
len(s2) # Returns 15

# To fix this issue, normalize the text with unicodedata

t1 = unicodedata.normalize('NFC', s1) #NFC = fully composed, use a single code point if possible
t2 = unicodedata.normalize('NFC', s2)
t1 == t2 # Asserts True
print(ascii(t1)) # Returns 'Spicy Jalape\xf1o'

t3 = unicodedata.normalize('NFD', s1) #NFD = fully decomposed, with use of combining characters
t4 = unicodedata.normalize('NFD', s2)
print(ascii(t3)) # Returns 'Spicy Jalapen\u0303o'

s = '\ufb01' # A single character
s # Returns 'ﬁ'
unicodedata.normalize('NFD', s) # Returns 'ﬁ'

# Notice how the combined letters are broken apart below with NFKC and NFKD.
unicodedata.normalize('NFKD', s) 
unicodedata.normalize('NFKC', s) # Both return 'fi'

t1 = unicodedata.normalize('NFD', s1) # Removal all diacritical marks
''.join(c for c in t1 if not unicodedata.combining(c)) # Returns 'Spicy Jalapeno'

# Combining tests a character to see if it is a combining character. 
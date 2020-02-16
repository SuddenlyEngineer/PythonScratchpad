import re

# The re module already has rudementary knowledge of Unicode character classes, like \d.

num = re.compile('\d+') 
num.match('123') # Here, ASCII digits. Returns an SRE_Match object
num.match('\u0661\u0662\u0663') # Likewise, returns an SRE_Match object.

# If you need to include specific Unicode characters in patterns, you can use the usual Unicode
# escape sequences for Unicode characters, like \uFFFF or \UFFFFFFF. 

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+') #Matches all characters in a few different Arabic code pages.

# It's a good idea to normalize / sanitize text to a standard form first. 
# Below, case-insensitive matching is combined with case folding.

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s) # Returns a match, an SRE_Match object
pat.match(s.upper()) # Returns nothing
s.uppser() # Returns 'STRASSE', case folds.compile

# For a more comprehensive solution, use the third party regex library.
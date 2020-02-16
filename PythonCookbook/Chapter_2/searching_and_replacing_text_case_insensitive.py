import re

# Want to do case-insensitive operations? Need to supply the re.IGNORECASE flag.

text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE) # Returns ['PYTHON', 'python', 'Python']
re.sub('python', 'snake', text, flags=re.IGNORECASE) # Returns 'UPPER snake, lower snake, Mixed snake'

def matchcase(word): # Use this function because replacing text will not match the case of the replaced text.
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE) # Returns 'UPPER SNAKE, lower snake, Mixed Snake'
import unicodedata
import sys

s = 'pýtĥöñ\fis\tawesome\r\n' #This is disgusting. First, get rid of the whitespace.

remap = {
    ord('\t') : ' ', # Remaps whitespace to space
    ord('\f') : ' ', # Likewise
    ord('\r') : None # Deleted carriage return
}
a = s.translate(remap) # Returns 'pýtĥöñ is awesome\n'

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a) # Returns 'pýtĥöñ is awesome\n'
b.translate(cmb_chrs) # Returns 'python is awesome\n'

# The dictionary above mapped every unicode combining character to None.
# The original input is normalized and decomposed using unicode.normalize.
# Then translate deletes all accents. Can do the same with control characters.

# Below is a translation table that maps all Unicode decimal digit characters to ASCII.
digitmap = { c: ord('0') + unicodedata.digit(chr(c)) 
for c in range(sys.maxunicode) 
if unicodedata.category(chr(c)) == 'Nd' }

len(digitmap) # 460

x = '\u0661\u0662\u0663' # Arabic digits
x.translate(digitmap) # Returns '123'

# You can also do preliminary cleanup of the text, then use encode()/decode() to strip / alter text.

b = unicodedata.normalize('NFD', a)
b.encode('ascii', 'ignore').decode('ascii') # Returns 'python is awesome\n'

# str.replace() is often the fastest approach, even if called multiple times; translate() is slow.

def clean_spaces(s): # Much faster
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s

# translate() is fast for nontrivial character-to-character remapping or deletion. 
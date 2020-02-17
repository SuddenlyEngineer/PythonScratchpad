import base64

s = b'hello' # Some byte data
a = base64.b64encode(s) # Returns b'aGVsbG8='
base64.b64decode(a) # Returns b'Hello'

# Only use Base64 encoding on byte-oriented data like byte strings and byte arrays.
# Output is always byte strings.

a = base64.b64encode(s).decode('ascii') # Returns 'aGVsbG8='

# Same caveats about decoding and unicode strings.
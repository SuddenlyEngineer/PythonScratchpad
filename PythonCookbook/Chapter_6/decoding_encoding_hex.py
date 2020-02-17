import binascii
import base64

s = b'hello' # Initial byte string

h = binascii.b2a_hex(s) # Returns b'68656c6c6f'
binascii.a2b_hex(h) # Returns b'hello'

h = base64.b16encode(s) # Returns b'68656C6C6F'
b = base64.b16decode(h) # Returns b'hello'

# Difference between the two is case folding. Base64 operate with uppercase hex letters; binascii use either case.
# Output is always a bytestring. Decoding to unicode requires another step.
print(h.decode('ascii')) # Returns 68656C6C6F

# When decoding, b16decode() and a2b_hex() accept bytes or unicode strings, but strings must only contain ASCII-encoded hex digits.
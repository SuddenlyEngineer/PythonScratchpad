import struct

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004' # 16-element byte string holding a 128-bit integer

# See below to interpret the bytes as an integer.
len(data) # 16
int.from_bytes(data, 'little') # Returns 69120565665751139577663547927094891008
int.from_bytes(data, 'big') # Returns 94522842520747284487117727783387188

# To interpret a large int back into a byte string, use int.to_bytes()
x = 94522842520747284487117727783387188
x.to_bytes(16, 'big') # Returns b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
x.to_bytes(16, 'little') # Returns b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'

# Could use struct, but the size of integers that can be unpacked is limited.
# So multiple values must be unpacked and combined.

hi, lo = struct.unpack('>QQ', data)
(hi << 64) + lo # Returns 94522842520747284487117727783387188

# Byte order, little or big, indicates whether bytes that make up the integer value are 
# listed from least to most significant or the other way around.

x = 0x01020304
x.to_bytes(4, 'big') # Returns b'\x01\x02\x03\x04'
x.to_bytes(4, 'little') # Returns b'\x01\x02\x03\x04'

# To pack an integer into a byte string, use int.bit_length()
x = 523 ** 23 
x.bit_length # 208
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
x.to_bytes(nbytes, 'little') # Returns b'\x03X\xf1\x82iT\x96\xac\xc7c\x16\xf3\xb9\xcf...\xd0'
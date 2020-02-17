import os
import sys

# Wrapping a higher-level Python file object around an integer file descriptor corresponding to an already open I/O channel.

fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT) # Open a low-level file descriptor

f = open(fd, 'wt') # Turn into a proper file, supply the integer file descriptor intead of a file name.
f.write('hello world\n')
f.close()

# When the high-level file object is closed or destroyed, the underlying file descriptor will also be closed.
# To avoid this, add the closedfd=False to open()

# Below is a socket example. Only works on Unix-based systems
# For cross-platform use, use makefile() instead.

from socket import socket, AF_INET, SOCK_STREAM

def echo_client(client_sock, addr):
    print('Got connection from', addr)

    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                         closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                          closefd=False)

    # Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

bstdout = open(sys.stdout.fileno(), 'wb', closefd=False) # Create a binary-mode file for stdout.
bstdout.write(b'Hello World\n')
bstdout.flush()


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = '' # Create a variable for a possible error message; this is the first change in relation to mirror_gen
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError: # Handle ZeroDivisionError by setting an error message.
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write # Undo monkey-patching of sys.stdout.write
        if msg:
            print(msg) # Display error message if set.
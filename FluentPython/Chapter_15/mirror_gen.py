import contextlib


@contextlib.contextmanager # Apply the context decorator.
def looking_glass():
    import sys
    original_write = sys.stdout.write # Preserve original sys.stdout.write method. 

    def reverse_write(text): # Define custom reverse_write function; original_write will be available in the closure.
        original_write(text[::-1])

    sys.stdout.write = reverse_write # Replace sys.stdout.write with reverse_write.
    yield 'JABBERWOCKY' # Yield the value that will be bound to the target variable in the as clause of the with statement. This function pauses at this point with the body of the with executes.
    sys.stdout.write = original_write # When control exits the with block in any way, execution continues after the yield; here the orignal sys.stdout.write is restored.

# If an exception is raised, this really breaks. Hard.
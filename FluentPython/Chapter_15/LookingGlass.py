class LookingGlass:

    def __enter__(self): # Python invokes __enter__ with no arguments besides self.
        import sys
        self.original_write = sys.stdout.write # Hold the original sys.stdout.write method in an instance attribute for later use.
        sys.stdout.write = self.reverse_write # Monkey-patch sys.stdout.write, replacing it with our own method.
        return 'JABBERWOCKY' # Return the 'JABBERWOCKY' string just so we have something to put in the target variable what.

    def reverse_write(self, text): # Our replacement to sys.stdout.write reverses the text argument and calls the original implementation. 
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback): # Python calls __exit__ with None, None, None if all went well; if an exception is raised, the three arguments get the exception data, as described next.
        import sys # It's cheap to impoprt modules again because Python catches them.
        sys.stdout.write = self.original_write # Restore the original method to sys.stdout.write.
        if exc_type is ZeroDivisionError: # If the exception is not None and its type is ZeroDivisionError, print a message
            print('Please DO NOT divide by zero!')
            return True  # and return True to tell the interpreter that the exception was handled.
        # If __exit__ returns None or anything but True, any exception raised in the with block will be propogated.
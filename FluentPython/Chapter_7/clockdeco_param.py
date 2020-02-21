import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT): # Clock is our parameterized decorator factory.
    def decorate(func): # Decorate is the actual decorator
        def clocked(*_args): # Clocked wraps the decorated function.
            t0 = time.time() 
            _result = func(*_args) # _result is the actual result of the decorated function.
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args) # _args holds the actual arguments of clocked, while args in str is used for display.
            result = repr(_result) # result is the str representation of _result, for display.
            print(fmt.format(**locals())) # Using **locals() here allows any local variable of clocked to be referenced in the fmt. 
            return _result # Clocked will replace the decorated function, so it should return whatever that function returns.
        return clocked # Decorate returns clocked.
    return decorate # Clock returns decorate.

if __name__ == '__main__':

    @clock() # In this self test, clock() is called without arguments, so decorator applied will use the default format str.
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)
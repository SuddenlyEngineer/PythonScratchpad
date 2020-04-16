"""
A coroutine to compute a running average

    >>> coro_avg = averager()  # Call averager(), creating a generator object that is primed inside the primer function of the coroutine decorator.
    >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(coro_avg)  # getgeneratorstate reports GEN_SUSPENDED, meaning that the coroutine is ready to receive a value.
    'GEN_SUSPENDED'
    >>> coro_avg.send(10)  # You can immediately start sending values to coro_avg: that's the point of the decorator.
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0

"""

from FluentPython.Chapter_16.coroutil import coroutine # Import the coroutine decorator

@coroutine # Apply it to the averager function.
def averager(): # The body of the function is exactly the same as coroaverager0.
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break # In order to return a value, a coroutine must terminate normally; this is why this version of averager has a condition to break out of its accumulating loop.
        total += term
        count += 1
        average = total/count
    return Result(count, average) # Return a namedtuple with the count and average. Before Python 3.3, it was a syntax error to return a value in a generator function.

if __name__ == "__main__":
    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(10) # This version does not yield values
    coro_avg.send(30)
    coro_avg.send(6.5)
    try:
        coro_avg.send(None) # Sending None terminates the loop, causing the coroutine to end by returning the result. As usual, the generator object raises StopIteration. The value attribute of the exception carries the value returned.
    except StopIteration as exc:
        result = exc.value
    print(result)
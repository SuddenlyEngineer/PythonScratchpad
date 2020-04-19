import asyncio
import itertools
import sys


@asyncio.coroutine # Coroutines intended for use with asyncio should be decorated with this. It isn't mandatory, but highly advisable.
def spin(msg): # Here we don't need the signal arguument that was used to shut down the thread in the spin function of the other spinner.
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1) # Use yield from asyncio.sleep(.1) instead of just time.sleep(.1) to sleep without blocking the event loop.
        except asyncio.CancelledError: # If asyncio.CancelledError is raised after spin wakes up, it's because cancellation was requested, so exit the loop.
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function(): # slow_function is now a coroutine, and uses yield from to let the event loop process while this coroutine pretends to do I/O by sleeping.
    # Pretend to wait a long time for I/O
    yield from asyncio.sleep(3) # The yield from asyncio.sleep(3) expression handles the control flow to the main loop, which will resume this cororutine after the sleep delay.
    return 42


@asyncio.coroutine
def supervisor(): # supervisor is now a coroutine as well, so it can drive slow_function with yield from. 
    spinner = asyncio.async(spin('thinking!')) # asyncio.async() schedules the spin coroutine to run, wrapping it in a Task object, which is returned immediately. 
    print('spinner object:', spinner) # Display the Task object. The output looks like <Task pending coro=<spin() running at spinner_asyncio.py:12>>.
    result = yield from slow_function() # Drive the slow_function(). When that is done, get the returned value. Meanwhile, the event loop will continue running because slow_function ultimately uses yield from asyncio.sleep(3) to hand control back to the main loop.
    spinner.cancel() # A Task object can be cancelled; this raises asyncio.CancelledError at the yield line where the coroutine is currently suspended. The coroutine may catch the exception and delay or even refuse to cancel.
    return result


def main():
    loop = asyncio.get_event_loop() # Get a reference to the event loop
    result = loop.run_until_complete(supervisor()) # Drive the supervisor coroutine to completion; the return value of the coroutine is the return value of this call.
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
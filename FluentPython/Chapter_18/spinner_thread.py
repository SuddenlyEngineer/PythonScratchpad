import threading
import itertools
import time
import sys


class Signal: # This class defines a simple mutable object with a go attribute we'll use to control the thread from outside.
    go = True


def spin(msg, signal):  # This function will run in a separate thread. The signal argument is an instance of the Signal class just defined.
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):  # This is actually an infinite loop because itertools.cycle produces items cycling from the given sequence forever.
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # The trick to do text-mode animation: move the cursor back with backspace characters(\x08).
        time.sleep(.1)
        if not signal.go:  # If the go attribute is no longer True, exit the loop
            break
    write(' ' * len(status) + '\x08' * len(status)) # Clear the status line by overwriting with spaces and moving the cursor back to the beginning.


def slow_function():  # Imagine this is some costly computation
    # pretend waiting a long time for I/O
    time.sleep(3)  # Calling sleep will block the main thread, but crucially, the GIL will be released so the secondary thread will proceed.
    return 42


def supervisor():  # This function sets up the secondary thread, displays the thread object, runs the slow computation, and kills the thread.
    signal = Signal()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', signal))
    print('spinner object:', spinner)  # Display the secondary thread object. The output looks like <Thread(Thread-1, initial)>.
    spinner.start()  # Start the secondary thread.
    result = slow_function()  # Run slow_function; this blocks the main thread. Meanwhile, the spinner is animated by the secondary thread.
    signal.go = False  # Change the state of the signal; this will terminate the for loop inside the spin function.
    spinner.join()  # Wait until the spinner thread finishes.
    return result


def main():
    result = supervisor()  # Run the supervisor function.
    print('Answer:', result)


if __name__ == '__main__':
    main()
from time import sleep, strftime
from concurrent import futures

def display(*args): # This function simply prints whatever arguemnts it gets, preceded by a timestamp in the format HH:MM:SS.
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n): # loiter does nothing except display a message when it starts, sleep for n seconds, then display a message when it ends.
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10 # loiter return n * 10 so we can see how to collect results. 


def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers = 3) # Create a ThreadPoolExecutor with three threads.
    results = executor.map(loiter, range(5)) # Submit five tasks to the executor (because there are only three threads, only three of those tasks will start immediately; the calls loiter(0), loiter(1), loiter(2)); this is a nonblocking call.
    display('results:', results) # Immediately display the results of invoking executor.map: it's a generator.
    display('Waiting for individual results:')
    for i, result in enumerate(results): # The enumerate call in the for loop will implicitly invoke next(results), which in turn will invoke _f.result() on the (internal) _f future representing the first call, loiter(0). The result method will block until the future is done, therefore each iteration in this loop will have to wait for the next result to be ready.
        display('result {}: {}'.format(i, result))


main()

'''

[13:40:37] Script starting.
[13:40:37] loiter(0): doing nothing for 0s... # First thread executes loiter(0), so it will sleep for 0s and return before the second thread has a chance to start (usually).
[13:40:37] loiter(0): done.
[13:40:37] 	loiter(1): doing nothing for 1s... # loiter(1) and loiter(2) start immediately (because the thread pool has three workers, it can run three functions concurrently).
[13:40:37] 		loiter(2): doing nothing for 2s...
[13:40:37] 			loiter(3): doing nothing for 3s... # Because loiter(0) is done, the first worker is now available to start the fourth thread for loiter(3).
[13:40:37] results: <generator object Executor.map.<locals>.result_iterator at 0x000002306728E740> # This shows that the results return by executor.map is a generator; nothing so far would block, regardless of the number of tasks and the max_workers setting.
[13:40:37] Waiting for individual results:
[13:40:37] result 0: 0 # This is where execution may block, depending on the parameters given to the loiter calls: the __next__ method of the reuslts generator must wait until the first future is complete. In this case, it won't block because the call to loiter(0) finished before this loop started. Note that everything up to this point happened within the same second. 
[13:40:38] 	loiter(1): done. # loiter(1) is done one second later. The thread is free to start loiter(4).
[13:40:38] 				loiter(4): doing nothing for 4s...[13:40:38]
result 1: 10 # The result of loiter(1) is shown: 10. Now the for loop will block waiiting for the result of loiter(2).
[13:40:39] 		loiter(2): done. # The pattern repeats: loiter(2) is done, its result is shown; same with loiter(3).
[13:40:39] result 2: 20
[13:40:40] 			loiter(3): done.
[13:40:40] result 3: 30
[13:40:42] 				loiter(4): done. # There is a 3s delay until loiter(4) is done, because it started at 15:56:51 and did nothing for 4s.
[13:40:42] result 4: 40

'''
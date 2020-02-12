import subprocess
import time
import os

result = subprocess.run(
    ['echo', 'Hello from the child process!'],
    capture_output=True,
    encoding='utf-8'
)

result.check_returncode()
print(result.stdout)

proc = subprocess.Popen(['sleep', '1'])
while proc.poll() is None:
    print('Working...')

    # Some time-consuming work here
    ...

print('Exit status', proc.poll())

start = time.time()
sleep_procs = []
for _ in range(10):
    proc = subprocess.Popen(['sleep', '1'])
    sleep_procs.append(proc)

for proc in sleep_procs:
    proc.communicate()

end = time.time()
delta = end - start
print(f'Finished in {delta:.3} seconds')
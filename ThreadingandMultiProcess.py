from multiprocessing import Process
from threading import Thread
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


threads = []
process = []
num_processes = os.cpu_count()
num_threads = 10
# create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    process.append(p)

for i in range(num_threads):
    p = Thread(target=square_numbers)
    threads.append(p)

# start
for p in process:
    p.start()

for p in threads:
    p.start()

# join
for p in process:
    p.join()
for p in threads:
    p.join()

print('end main')

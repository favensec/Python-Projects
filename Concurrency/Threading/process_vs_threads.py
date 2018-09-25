import threading
from multiprocessing import Process

import time
import os

def MyTask():
    print "Starting"
    time.sleep(2)

t0 = time.time()
threads = []

for i in range(10):
    thread = threading.Thread(target=MyTask)
    thread.start()
    threads.append(thread)

t1 = time.time()
print "Total time for creating 10 threads: {} seconds".format(t1-t0)
for thread in threads:
    thread.join()

t2 = time.time()
procs = []

for i in range(10):
    process = Process(target=MyTask)
    process.start()
    procs.append(process)

t3 = time.time()
print "Total time for creating 10 processes: {} seconds".format(t3-t2)

for proc in procs:
    proc.join()

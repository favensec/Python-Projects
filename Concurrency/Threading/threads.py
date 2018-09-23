#Starting a thread.

import threading
import time
import random

def executeThread(i):
    print "Thread {} started".format(i)
    sleepTime = random.randint(1,10)
    time.sleep(sleepTime)
    print "Thread {} finished executing".format(i)

for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i, ))
    thread.start()
    print "Active Threads: ", threading.enumerate()

#Inheriting from the thread class.
from threading import Thread

class myWorkerThread(Thread):
    def __init__(self):
        print "Hello World!"
        Thread.__init__(self)
    def run(self):
        print "Thread is now running!"
    
myThread = myWorkerThread()
print "Created Thread Object"
myThread.start()
print "Started my thread"
myThread.join()
print "Thread finished"
        

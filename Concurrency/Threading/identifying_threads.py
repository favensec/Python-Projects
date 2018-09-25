import threading
import time

def myThread():
    print "Thread {} starting".format(threading.currentThread().getName()) + "\n"
    time.sleep(10)
    print "Thread {} ending".format(threading.currentThread().getName()) + "\n"

for i in range(4):
    threadName = "Thread-" + str(i) + "\n"
    thread = threading.Thread(name=threadName, target=myThread)
    thread.start()

print "{}".format(threading.enumerate())
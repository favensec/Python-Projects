import threading
import time

#Execute our thread
def threadWorker():
    print "Thread has entered a 'Running' state."
    time.sleep(10)
    print "Thread is 'terminating'..."

thisThread = threading.Thread(target=threadWorker)
thisThread.start() #Thread is on a 'Starting' state
thisThread.join() #Thread is on a 'Dead' state
print "This thread has entered a 'Dead' state."
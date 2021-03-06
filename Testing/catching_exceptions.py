import sys
import threading
import time
import Queue

def myThread(queue):
    while True:
        try:
            time.sleep(2)
            raise Exception("Exception thrown in child thread {}".format(threading\
                                .current_thread()))
        except:
            queue.put(sys.exc_info())

    queue = queue.Queue()
    myThread = threading.Thread(target=myThread, args=(queue,))
    myThread.start()

    while True:
        try:
            exception = queue.get()
        except Queue.Empty:
            pass
        else:
            print(exception)
            break

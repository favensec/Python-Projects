import threading
import time

def standardThread():
    print "Starting standard thread"
    time.sleep(20)
    print "Ending standard thread"

def daemonThread():
    while True:
        print "Sending out heartbeat signal"
        time.sleep(2)

if __name__ == '__main__':
    standardThread = threading.Thread(target=standardThread)
    daemonThread = threading.Thread(target=daemonThread)
    daemonThread.setDaemon(True)
    daemonThread.start()

    standardThread.start()
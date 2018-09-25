import threading
import time

def ourThread(i):
    print "Thread {} started".format(i)
    time.sleep(i*2)
    print "Thread {} finished.".format(i)

def main():
    thread1 = threading.Thread(target=ourThread, args=(1, ))
    thread1.start()
    print "Is thread 1 finihsed?"

    thread2 = threading.Thread(target=ourThread, args=(2, ))
    thread2.start()
    thread2.join()
    print "Thread 2 finished"

if __name__ == '__main__':
    main()
import threading
import time
import random

def myThread(i):
    print "Thread {}: started".format(i)
    time.sleep(random.randint(1,5))
    print "Thread {}: finished".format(i)

#Let's slow it down.
def calculatePrimeFactors(n):
    primefac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primefac.append(d)
            n //= d
        d += 1
    if n > 1:
        primefac.append(n)
    return primefac

def executeProc():
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print (calculatePrimeFactors(rand))

def main():
    print "Starting..."
    t0 = time.time()

    threads = []
    for i in range(10):
        thread = threading.Thread(target=executeProc)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    t1 = time.time()
    totalTime = t1-t0
    print "Total Number of Active Threads: {}".format\
    (threading.active_count())
    print "Execution time: {}".format(totalTime)

if __name__ == '__main__':
    main()
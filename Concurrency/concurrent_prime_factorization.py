import time
import random

from multiprocessing import Process

def calculatePrimeFactors(n):
    primfac = []
    d = 2

    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac

    #Split workload from one batch of 10,000 calculations
    #into 10 batches of 1,000 calculations
def executeProc():
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print calculatePrimeFactors(rand)

def main():
    print "Starting number crunching"
    t0 = time.time()
    procs = []
    #Create process and start
    for i in range(10):
        proc = Process(target=executeProc, args=())
        procs.append(proc)
        proc.start()
    
    for proc in procs:
        proc.join()
    t1 = time.time()
    totalTime = t1 - t0
    print "Execution time: {}".format(totalTime)

if __name__ == '__main__':
    main()

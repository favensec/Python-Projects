from multiprocessing import Process
import time

def myWorker():
    t1 = time.time()
    print "Process started at: {}".format(t1)
    time.sleep(20) #Sleep for 20 seconds

myProcess = Process(target=myWorker) #Pass process to function myWorker
print "Process {}".format(myProcess)
myProcess.start() #Start process
print "Terminating Process..."
myProcess.terminate() #End process
myProcess.join()
print "Process terminated: {}".format(myProcess)



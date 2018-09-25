import threading
import time
import random

class Publisher(threading.Thread):
    def __init__(self, integers, condition):
        self.condition = condition
        self.integers = integers
        threading.Thread.__init__(self)

    def run(self):
        while True:
            integer = random.randint(0, 1000)
            self.condition.acquire()
            
            print "Condition acquired by publisher: {}".format(self.name)
            self.integers.append(integer)
            self.condition.notify()
            
            print "Condition released by publisher: {}".format(self.name)
            self.condition.release()
            time.sleep(1)

class Subscriber(threading.Thread):
    def __init__(self, integers, condition):
        self.integers = integers
        self.condition = condition
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.condition.acquire()
            print "Condition acquired by consumer: {}".format(self.name)
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print "{} Popped from list by consumer: {}".format(integer, self.name)
                    break
                print "Condition wait by {}".format(self.name)
                self.condition.wait()

        print "Consumer {} releasing condition".format(self.name)
        self.condition.release()

def main():
    integers = []
    condition = threading.Condition()

    #Our publisher
    pub1 = Publisher(integers, condition)
    pub1.start()

    #Our subscribers
    sub1 = Subscriber(integers, condition)
    sub2 = Subscriber(integers, condition)

    #Start subscribers
    sub1.start()
    sub2.start()

    #Join threads
    pub1.join()
    sub1.join()
    sub2.join()

if __name__ == '__main__':
    main()
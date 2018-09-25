import threading
import random
import time

class TicketSeller(threading.Thread):
    ticketsSold = 0

    def __init__(self, semaphore):
        threading.Thread.__init__(self)
        self.sem = semaphore
        print "Ticket seller started work"
    
    def run(self): 
        global ticketsAvailable

        running = True
        while running:
            self.randomDelay()
            self.sem.acquire()

            if(ticketsAvailable <= 0):
                running = False
            else:
                self.ticketsSold = self.ticketsSold + 1
                ticketsAvailable = ticketsAvailable - 1
                print "{} sold one ({} left)".format(self.getName(), ticketsAvailable)
                self.sem.release()
            
            print "Ticket sellet {} sold {} tickets in total".format(self.getName(), self.ticketsSold)

    def randomDelay(self):
        time.sleep(random.randint(0,4)/4)

#semaphore primitive
semaphore = threading.Semaphore()

#ticket allocaiton
ticketsAvailable = 10
    
#array of sellers
sellers = []

for i in range(4):
    seller = TicketSeller(semaphore)
    seller.start()
    sellers.append(seller)

for seller in sellers:
    seller.join()
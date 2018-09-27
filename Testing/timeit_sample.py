import timeit
import time

def function1():
    print "Function 1 is executing..."
    time.sleep(5)
    print "Functtion 1 is complete..."

def function2():
    print "Function 2 is executing..."
    time.sleep(6)
    print "Function 2 is complete..."

function1_time = timeit.Timer("function1()", setup="from __main__ import function1")
times = function1_time.repeat(repeat=2, number=1)
for t in times:
    print "{} seconds: ".format(t)

function2_time = timeit.Timer("function2()", setup="from __main__ import function2")
times = function2_time.repeat(repeat=2, number=1)
for t in times:
    print "{} seconds: ".format(t)
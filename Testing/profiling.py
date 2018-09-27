#Usage: python -m cProfile profiling.py

import collections

doubleEndedQueue = collections.deque('123456')

print "Deque: {}".format(doubleEndedQueue)

doubleEndedQueue.append('1')
print "Dequeue: {}".format(doubleEndedQueue)

doubleEndedQueue.append('6')
print "Deque: {}".format(doubleEndedQueue)
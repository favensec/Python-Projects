from collections import deque

import collections
import Queue

doubleEndedQueue = collections.deque('123456')

print "Dequeue: {}".format(doubleEndedQueue)

for item in doubleEndedQueue:
    print "Item {}".format(item)
    print "Left most element: {}".format(doubleEndedQueue[0])
    print "Right most element: {}".format(doubleEndedQueue[-1])

#Appending elements
print "Appending elements of double-ended queue."
print "Deque: {}".format(doubleEndedQueue)

doubleEndedQueue.append('1')
print "Deque: {}".format(doubleEndedQueue)

doubleEndedQueue.append('6')
print "Deque: {}".format(doubleEndedQueue)

#Removing elements from our queue
rightPop = doubleEndedQueue.pop()
print(rightPop)
print "Elements removed from right pop."
print "Deque: {}".format(doubleEndedQueue)

leftPop = doubleEndedQueue.popleft()
print(leftPop)
print "Elements removed from left pop."
print "Deque: {}".format(doubleEndedQueue)

#Inserting elements
insertElements = doubleEndedQueue.insert(5,5)
print "Inserting elements."
print "Deque: {}".format(insertElements)
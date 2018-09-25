import urllib
import time

t0 = time.time()

request = urllib.urlopen('http://www.example.com')
pageHtml = request.read()
t1 = time.time()
print "Total Time to Fetch Page: {} Seconds".format(t1-t0)

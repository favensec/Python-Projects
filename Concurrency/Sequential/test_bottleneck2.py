import urllib2
import time
from bs4 import BeautifulSoup

t0 = time.time()
request = urllib2.urlopen('http://www.example.com')
t1 = time.time()

print"Total Time To Fetch Page: {} Seconds".format(t1-t0)
soup = BeautifulSoup(request.read())

for link in soup.find_all('a'):
    print(link.get('href'))

t2 = time.time()
print "Total Execution Time: {} Seconds".format
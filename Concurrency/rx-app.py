import rx
from rx import Observable, Observer

class temperatureObserver(Observer):
    def on_next(self, x):
        print "The temperature is: %s degrees centigrade" % x

        if (x > 6):
            print "Warning: Temperature is exceeding recommended limit."

        if (x == 9):
            print "DataCenter is shutting down. Temperature is too high."

    def on_error(self, e):
        print "Error: %s" % e
    
    def on_completed(self):
        print "All Temps Read"

xs = Observable.from_iterable(range(10))
d = xs.subscribe(temperatureObserver())
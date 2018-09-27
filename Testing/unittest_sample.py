import unittest

def simpleFunction(x):
    return x + 1

class SimpleFunctionTest(unittest.TestCase):
    def setUp(self):
        print "This is run before all our tests have a change to execute."
    
    def tearDown(self):
        print "This is executed after all our tests have completed."

    def test_simple_function(self):
        print "Testing that our function works with positive tests."
        self.assertEqual(simpleFunction(2), 3)
        self.assertEqual(simpleFunction(234135145145432143214321432),
        234135145145432143214321433)
        self.assertEqual(simpleFunction(0), 1)

if __name__ == '__main__':
    unittest.main()
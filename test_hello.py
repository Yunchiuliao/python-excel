import unittest

from hello import Hello

class TestHello(unittest.TestCase):
    
    def testHelloWorld(self):
        hello = Hello().say()
        self.assertEqual("hello world", hello)
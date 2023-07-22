import unittest

from store import Store


class TestStore(unittest.TestCase):

    def setUp(self):
        self.testStore = Store()
        
    def testHeaderFirstColumn(self):
        actual = self.testStore.getHeaderFirstColumn()
        expected = "店名"
        self.assertEqual(expected,actual)
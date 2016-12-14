import unittest

class TestCase(unittest.TestCase):

    def test_trangle(self):
        lst = [1, 1, 1]

        print sum(lst.count(x) for x in lst)
        pass
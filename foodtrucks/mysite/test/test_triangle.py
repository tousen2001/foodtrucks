import unittest


class TestCase(unittest.TestCase):

    def test_trangle(self):
        lst = [1, 1, 3, 3, 5]

        print len(set(lst)), [{i : lst.count(i)} for i in set(lst)]
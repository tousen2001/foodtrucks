import unittest


class TestCase(unittest.TestCase):

    def test_trangle(self):
        lst = [1, 1, 3, 3, 5]

        print len(set(lst)), [{i : lst.count(i)} for i in set(lst)]

    def test_python(self):
        print repr({'key': 'value'})

        print eval("{'key': 'value'}")['key']

        print 3.0 % 10

        print "hello world".title()
        print "hello world".capitalize()

        print cmp([1, 2, 3], [1, 2, 3])

        print [1, 3, 3, 4].index(3)

        print [1, 3, 3, 4].pop(3)


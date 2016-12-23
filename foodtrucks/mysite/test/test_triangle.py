import unittest

class TestCase(unittest.TestCase):

    def test_trangle(self):
        lst = [1, 1, 1]

        print len(set(lst))
        # 6 / 3 = 2
        # 2 * 2 * 3 = 12
        ##
        # 6 / 2 = 3
        # 3 * 3 * 2 + (6 - (3 * 2)) = 18
        # 2 * 2 * 2 + (6 - (2 * 2)) = 10
        # 3 * 3 + 2 * 2 + (6 - (3 + 2)) =
        ##
        # 6 / 1 = 6
        # 6 * 6 * 1 = 36
        # 5 * 5 * 1 + (6 - 5) = 26
        # 4 * 4 * 1 + (6 - 4) = 18
        # 3 * 3 * 1 + (6 - 3) = 12
        # 2 * 2 * 1 + (6 - 2) = 8


        # 6, [1, 2, 3, 4, 5, 6]
        # 1, [1, 1, 1, 1, 1, 1]
        # 2, [1, 1, 1, 1, 1, 2] (5 * 5 + 1)
        # 3, [1, 1, 1, 1, 2, 3] (4*4+2 = 18) [1, 1, 2, 2, 3, 3] (2*2 + 2*2 + 2*2 = 12)
        # 4, [1, 1, 1, 2, 3, 4], [1, 1, 2, 2, 3, 4]

        #self.get_result(sum(lst.count(x) for x in lst), len(lst))

    @staticmethod
    def get_result(num, icount):
        if icount * icount == num:
            print "this is the same sides shape."

        itype = icount / 2

        print "it has {0} duplication types.".format(itype)
        for i in range(0, itype + 1):
            print "for type {0}".format(i)
            if i == 0:
                print 'if num is {0}'.format(icount), "It means have 0 duplicate sides for type 0"
                continue

            for j in range(2, icount/i + 1):
                print "if num is {0}".format(j * j * i + (icount - j * i)), "It means have {0} duplicate sides for type {1}".format(j, i)

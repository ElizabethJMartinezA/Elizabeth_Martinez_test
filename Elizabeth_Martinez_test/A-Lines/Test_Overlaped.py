import unittest
from Overlaped_Lines import OverlapedLines


class OverLap_Test(unittest.TestCase):

    
    def OverLap_Sorted(self):
        result = OverlapedLines((1, 5), (2, 6))
        self.assertEqual(result, "The line (1, 5) and the line (2, 6) overlap")

    def OverLap_nonSorted(self):
        result = OverlapedLines((5, 1), (2, 6))
        self.assertEqual(result, "The line (1, 5) and the line (2, 6) overlap")
    
    def OverLap_nonSortedNeg(self):
        result = OverlapedLines((-1, -5), (-6, -2))
        self.assertEqual(result, "The line (-5, -1) and the line (-6, -2) overlap")

    def nonOverLap_Sorted(self):
        result = OverlapedLines((1, 5), (8, 6))
        self.assertEqual(result, "The line (1, 5) and the line (2, 8) does not overlap")

    def nonOverLap_nonSorted(self):
        result = OverlapedLines((5, 1), (8, 6))
        self.assertEqual(result, "The line (1, 5) and the line (2, 8) does not overlap")
    
    def nonOverLap_nonSortedNeg(self):
        result = OverlapedLines((-1, -5), (-8, -6))
        self.assertEqual(result, "The line (-5, -1) and the line (-8, -6) does not overlap")

    def nonOverLap_SortedPosNeg(self):
        result = OverlapedLines((-1, 0), (6, 2))
        self.assertEqual(result, "The line (-1, 0) and the line (2, 6) does not overlap")


if __name__ == '__main__':
    unittest.main()
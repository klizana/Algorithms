import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_worst_case(self):
        a = merge_sort([6,5,4,3,2,1])
        self.assertEqual(a,[1,2,3,4,5,6])
    
    def test_best_case(self):
        a = merge_sort([1,2,3,4,5,6])
        self.assertEqual(a,[1,2,3,4,5,6])
        
if __name__ == '__main__':
    unittest.main()
        

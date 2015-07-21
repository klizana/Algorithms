import unittest
from counting_inversions import sort_and_count

class TestCountingInversions(unittest.TestCase):

    def test_count_full_reverse_inversion(self):
        _, res = sort_and_count([6,5,4,3,2,1])
        self.assertEqual(res,15)
    
    def test_count_none_reverse_inversion(self):
        _, res = sort_and_count([1,2,3,4,5,6])
        self.assertEqual(res,0)
    
    def test_count_inversion_large_input(self):
        a = []
        with open('tests/counting_inversions.txt', 'r') as f:
            for line in f:
                a.append(int(line))
        f.closed

        _, res = sort_and_count(a)
        
        self.assertEqual(res,2407905288)


if __name__ == '__main__':
    unittest.main()

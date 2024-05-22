import unittest
from algorithm.merge_sort_on_array import recursive_merge_sort

class TestMergeSort(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(recursive_merge_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(recursive_merge_sort([5]), [5])

    def test_already_sorted_array(self):
        self.assertEqual(recursive_merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(recursive_merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_array(self):
        self.assertEqual(recursive_merge_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_duplicate_elements_array(self):
        self.assertEqual(recursive_merge_sort([1, 2, 2, 3, 4, 4, 5]), [1, 2, 2, 3, 4, 4, 5])

if __name__ == '__main__':
    unittest.main()
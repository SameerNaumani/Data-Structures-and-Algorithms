import unittest
from sorting import mo3_quickSort

class TestGenerate(unittest.TestCase):
   
    #test to see if size is generated correctly
    def test_size(self):
        alist = [54,26,93,17,77,31,44,55,20]
        mo3_quickSort(alist)
        result = len(alist)
        
        self.assertEqual(result, 9)
   

    #Test to see if sorting is done correctly
    def test_sort(self):
        alist = [54,26,93,17,77,31,44,55,20]
        mo3_quickSort(alist)
        result = alist
        self.assertEqual(result, [17, 20, 26, 31, 44, 54, 55, 77, 93])
        
    def test_sort3(self):
        alist = [22,33,54,26,93,17,77,31,44,55,20]
        mo3_quickSort(alist)
        result = alist
        self.assertEqual(result, [17, 20,22, 26, 31, 33, 44, 54, 55, 77, 93])
        
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # if running the above from the REPL use unittest.main() instead
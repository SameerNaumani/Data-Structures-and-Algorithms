import unittest
from mySolution import power
from mySolution import powerH
from mySolution import C

class TestGenerate(unittest.TestCase):
    def test_power(self):
        data = power(2 , 3)
        self.assertEqual(data, 8)
    
    def test_power2(self):
        data2 = power(4, 3)
        self.assertEqual(data2,64)
        
    def test_powerH(self):
        data3 = powerH(5,2)
        self.assertEqual(data3,25)
        
    def test_powerH2(self):
        data = powerH(6,3)
        self.assertEqual(data, 216)
        
    def test_C(self):
        data = C(4,2)
        self.assertEqual(data, 6)
        
    def test_C2(self):
        data = C(5,2)
        self.assertEqual(data, 10)
        
    def test_C3(self):
        data = C(2,4)
        self.assertEqual(data, "assert k>=0 and k<=")
    

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # if running the above from the REPL use unittest.main() instead
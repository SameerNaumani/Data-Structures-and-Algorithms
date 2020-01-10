import unittest
from parserTools import parse

class TestGenerate(unittest.TestCase):
 
    def test_1(self):
        x= [['4', '+', '3'], '*', '7']
        result = parse(x)
        self.assertEqual(result, ['*', ['+', ['4', [], []], ['3', [], []]], ['7', [], []]])
       
       
    
    def test_2(self):
        x = ['2', '!']
        result = parse(x)
     
        self.assertEqual(result, ['!', ['2', [], []], []])

    
    def test_3(self):
        x=['3','/','6','-', '9']
        result = parse(x)
        
        self.assertEqual(result, ['-', ['/', ['3', [], []], ['6', [], []]], ['9', [], []]])
     
   
    def test_4(self):
        x=['4', '+', '3', '*', '7']
        result = parse(x)
        
        self.assertEqual(result, ['+', ['4', [], []], ['*', ['3', [], []], ['7', [], []]]])
       
        
        
    def test_6(self):
        x = ['4', '+', [['3', '+', '1'], '!']]
        result = parse(x)
        
        self.assertEqual(result,  ['+', ['4', [], []], ['!', ['+', ['3', [], []], ['1', [], []]], []]])
        
    def test_6(self):
        x = [['4'], '+', ['3'], '+', '6']
        result = parse(x)
        
        self.assertEqual(result, ['+', ['+', ['4', [], []], ['3', [], []]], ['6', [], []]])
       



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # if running the above from the REPL use unittest.main() instead
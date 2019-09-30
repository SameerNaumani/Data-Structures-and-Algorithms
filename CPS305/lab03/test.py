import unittest
from mySolution import doMath
from mySolution import infixToPostfixEval

class TestGenerate(unittest.TestCase):

  ######## test do_math ########3
    def test_math(self):
        data = doMath("*" , 4, 4)
        self.assertEqual(data, 16)
    
    def test_math2(self):
        data2 = doMath("-", 10,4)
        self.assertEqual(data2,6)
        
    def test_math3(self):
        data3 = doMath("/",15,5)
        self.assertEqual(data3,3)
        
    def test_Eval(self):
        data = infixToPostfixEval("( 2 + 2 ) ! + 8")
        self.assertEqual(data, ('2 2 + ! 8 +', 'Evaluates to: ', 32))
        
    def test_Eval2(self):
        data = infixToPostfixEval("A * B + C * D")
        self.assertEqual(data, "Cannot be evaluated")
        
    def test_Eval3(self):
        data = infixToPostfixEval("2 * B + C * D")
        self.assertEqual(data, "Cannot be evaluated")
        
        
    

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # if running the above from the REPL use unittest.main() instead
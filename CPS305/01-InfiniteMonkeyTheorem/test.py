import unittest
from mySolution import generate
from mySolution import calcScore

class TestGenerate(unittest.TestCase):

  ######## test to see if the generator generates the correct number of terms ########3
    def test_generate(self):
        target = "methinks it is like a weasel"
        lenS = len(target)
        print(lenS)
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        lenA = len(alphabet)
        for i in range(10):
            string = generate(lenS, lenA, alphabet)
            print(len(string))
            self.assertEqual(len(string), lenS, "Should be equal to 28")
       
    def test_score(self):
        data = calcScore("heddo", "hello")
        self.assertTrue(50.0)
    

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # if running the above from the REPL use unittest.main() instead
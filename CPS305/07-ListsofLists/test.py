import unittest
from eval import evalTree
from eval import getDict

class TestGenerate(unittest.TestCase):
 
    def test_1(self):
        test1Tree=["10",[],[]]
        test1Environment=[["a",10],["b",20],["c",30]]
        self.assertEqual(evalTree(test1Tree,test1Environment),'10')
    
    def test_2(self):
        test2Tree=["x1",[],[]]
        test2Environment=[["a",10],["x1",30]]
     
        self.assertEqual(evalTree(test2Tree,test2Environment),30)

    
    def test_3(self):
        test3Tree=["+",["a",[],[]],["*",["b",[],[]],["c",[],[]]]]
        test3Environment=[["a",10],["b",20],["c",30]]
        self.assertEqual(evalTree(test3Tree,test3Environment),610)

   
    def test_4(self):
        test4Tree=["*",["b",[],[]],["c",[],[]]]
        test4Environment=[["a",10],["b",20],["c",30]]
        self.assertEqual(evalTree(test4Tree,test4Environment),600)
       
        
    def test_5(self):
        test2Tree=["x1",[],[]]
        test2Environment=[["a",10],["x1",30]]
        dicts = getDict(test2Environment)
        result = dicts.get((test2Tree[0]))
        
        self.assertEqual(result, 30)
       


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # if running the above from the REPL use unittest.main() instead
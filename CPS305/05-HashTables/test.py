import unittest
from hashing import HashTable

class TestGenerate(unittest.TestCase):
    #Create test cases that test putting key-data pairs in the table before table resizing, and then getting that data after tableresizing.
    
    #Test if the size remains 11 as long as the max threshold is not reached by putting in elements
    def test_size(self):
        H = HashTable()
        H[54]="cat"
        H[26]="dog"
        H[93]="lion"
        H[17]="tiger"
        H[77]="bird"
        H[31]="cow"
        
        self.assertEqual(H.size, 11)
   

    #Test if the size actually doubles when 80% of max threshold is reached by putting in elements
    def test_growth(self):
        H = HashTable()
        H[54]="cat"
        H[26]="dog"
        H[93]="lion"
        H[17]="tiger"
        H[77]="bird"
        H[31]="cow"
        H[44]="goat"
        H[55]="whale" #8 
        H[20]="chicken" #9
     
        self.assertEqual(H.size, 23)
    
    #Test getting the data before resize
    def test_getData(self):
        H = HashTable()
        H[54]="cat"
        H[26]="dog"
        H[77]="bird"
        H[31]="cow"
        H[44]="goat"
        H[55]="whale" #8 
        H[20]="chicken" #9
        
        self.assertEqual(H[20], 'chicken')
    
    #Test getting the data after resize 
    def test_getData2(self):
        H = HashTable()
        H[54]="cat"
        H[26]="dog"
        H[93]="lion"
        H[17]="tiger"
        H[77]="bird"
        H[31]="cow"
        H[44]="goat"
        H[55]="whale" #8 
        H[20]="chicken" #9
        
        self.assertEqual(H[20], 'chicken')
        
    def test_getData3(self):
        H = HashTable()
        H[54]="cat"
        H[26]="dog"
        H[93]="lion"
        H[17]="tiger"
        H[77]="bird"
        H[31]="cow"
        H[44]="goat"
        H[55]="salamander"
        H[20]="chicken"
        H[21]= "whale"    #10
        H[34] = "chihuahua" #11
        H[45] = "mammoth" #12 
        
        self.assertEqual(H.slots[2], None)
        
    #Check to see if it resizes to a prime number for the third resize       
    def test_getData4(self):
        H = HashTable()
        H[54]="cat"
        H[26]="dog"
        H[93]="lion"
        H[17]="tiger"
        H[77]="bird"
        H[31]="cow"
        H[44]="goat"
        H[55]="salamander"
        H[20]="chicken"
        H[21]= "whale"    #10
        H[34] = "chihuahua" #11
        H[45] = "mammoth" #12 
        H[72] = "charizard"
        H[33] = "pikachu"
        H[56] = "raptor"
        H[79] = "BlueJay"
        H[99] = "Dragon" #17
        H[61] = "Bat" #18
        H[68] = "Batman" #19
         
        self.assertEqual(H.size, 47)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # if running the above from the REPL use unittest.main() instead
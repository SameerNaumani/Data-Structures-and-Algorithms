import copy 
import sympy

class HashTable:
    def __init__(self, size = 11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.maxLoadFactor = 0.80
        self.count = 0
    
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))            
            
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            self.count += 1
            self.checkGrow()
            
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                    self.count += 1
                    self.checkGrow()
                else:
                    self.data[nextslot] = data #replace
       

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                           not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def checkGrow(self):
        if self.count > self.maxLoadFactor * self.size:
            self.grow()
    
    def grow(self):
        newSize = 2*self.size 
        if (newSize%2 == 0):
            newSize = newSize + 1
        while(sympy.isprime(newSize) == 'false'):
            newSize += 2
        H2 = HashTable(newSize)
        for key in self.slots:
            if key != None:
                H2.put(key, self.get(key))
      
        self.size = newSize
        self.slots = copy.deepcopy(H2.slots)
        self.data = copy.deepcopy(H2.data)
        del H2
    
    

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)
class HashTable:
    def __init__(self, size = 11):
        self.MAXLOADFACTOR = 0.75
        self.MINLOADFACTOR = 0.25
        self.MINSIZE = size
        self.size = size
        self.totalItems = 0
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            self.totalItems += 1
            self.checkGrow()
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                    self.totalItems += 1
                    self.checkGrow()
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key):
        if isinstance(key, int):
            return key % self.size
        else:
            s = str(key)
            return sum([ord(c) for c in s]) % self.size

  def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def remove(self, key):
        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] == None:
            return False

        else:
            if self.slots[hashvalue] == key:
                self.slots[hashvalue] = None
                self.data[hashvalue] = None
                self.totalItems -= 1
                self.checkShrink()

            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    return False
                else:
                    self.slots[nextslot] = None
                    self.data[nextslot] = None
                    self.totalItems -= 1
                    self.checkShrink()

    def checkGrow(self):

        if self.totalItems > self.MAXLOADFACTOR * self.size:
                self.grow()

    def grow(self):
        newSize = 2 * self.size
        newHashTable = HashTable(newSize)
        for key in self.slots:
            if key != None:
                newHashTable.put(key, self.get(key))

        self.size = newSize
        self.slots = copy.deepcopy(newHashTable.slots)
        self.data = copy.deepcopy(newHashTable.data)

        del newHashTable

    def checkShrink(self):
        if self.totalItems < self.MINLOADFACTOR * self.size and self.size >= self.MINSIZE * 2:
            self.shrink()

    def shrink(self):
        newSize = self.size // 2
        newHashTable = HashTable(newSize)

        for key in self.slots:
            if key != None:
                newHashTable.put(key, self.get(key))

        self.size = newSize
        self.slots = copy.deepcopy(newHashTable.slots)
        self.data = copy.deepcopy(newHashTable.data)
        del newHashTable

    def clearTable(self, size = 11):
        self.MAXLOADFACTOR = 0.75
        self.MINLOADFACTOR = 0.25
        self.MINSIZE = size
        self.size = size
        self.totalItems = 0
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __str__(self):
        s=''
        for k in self.slots:
            if k != None:
                s = s + str(k) + ': ' + str(self.get(k)) + '\n'

        return s[:-1]
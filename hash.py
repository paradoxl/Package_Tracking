class hashMap:
    def __int__(self,initCap = 10):
        self.table = []
        for i in range (initCap):
            self.table.append([])


    def insert (self, key, item):
        bucket = hash(key)%len(self.table)
        list = self.table[bucket]

        for keyPair in list:
            if keyPair[0] == key:
                keyPair[1] = item
                return True
            value = [key,item]
            list.append(value)
            return True

    def search (self, key):
        bucket = hash(key) % len(self.table)
        list = self.table[bucket]

        for keyPair in list:
            if keyPair[0] == key:
                return keyPair[1]
            return None


    def delete (self, key):
        bucket = hash(key) % len(self.table)
        list = self.table[bucket]

        if key in list:
            list.remove(key)


    

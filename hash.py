class HashTable:

    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        #
        bucket = hash(key) % len(self.table)
        hashList = self.table[bucket]

        for keyPair in hashList:
            # print (key_value)
            if keyPair[0] == key:
                keyPair[1] = item
                return True

        key_value = [key, item]
        hashList.append(key_value)
        return True

    def search(self, key):
        bucket = hash(key) % len(self.table)
        hashList = self.table[bucket]

        for keyPair in hashList:
            if keyPair[0] == key:
                return keyPair[1]
        return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        hashList = self.table[bucket]

        for keyPair in hashList:
            if keyPair[0] == key:
                hashList.remove([keyPair[0], keyPair[1]])

test = HashTable()
test.insert(1,1)
print(test.table)
# Class to hold hashtable/spicy dictionary
class HashTable:
    def __init__(self, initial_capacity=10):
        self.initial_capacity = initial_capacity
        self.hashTable = self.generate()
    def generate(self):
        return [[] for _ in range(self.initial_capacity)]
    # Time Complexity O(N)
    def set (self, key,value):
        hashKey = hash(key) % self.initial_capacity
        bucket = self.hashTable[hashKey]
        found = False
        for i,record in enumerate(bucket):
            recordKey, recordValue = record
            if recordKey == key:
                found = True
                break
        if found:
            bucket[i] = (key,value)
        else:
            bucket.append((key,value))
    # Time Complexity O(N)
    def getValue(self,key):
        hashKey = hash(key) % self.initial_capacity
        bucket = self.hashTable[hashKey]
        found = False
        for i, record in enumerate(bucket):
            recordKey, recordValue = record
            if recordKey == key:
                found = True
                break
        if found:
            return recordValue
        else:
            return None
    # Time Complexity O(N)
    def removeValue(self,key):
        hashKey = hash(key) % self.initial_capacity
        bucket = self.hashTable[hashKey]
        found = False

        for i, record in enumerate(bucket):
            recordKey, recordValue = record

            if recordKey == key:
                found = True
                break
            if found:
                bucket.pop(i)
            return
    def __str__(self):
        return "".join(str(item) for item in self.hashTable)




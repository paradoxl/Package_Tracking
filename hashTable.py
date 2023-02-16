
# Class to hold hashtable/spicy dictionary
class HashTable:
    def __init__(self, initial_capacity=10):
        self.initial_capacity = initial_capacity
        self.hash_table = self.create_bucket()
    def create_bucket(self):
        return [[] for _ in range(self.initial_capacity)]

    def set (self, key,value):
        hashKey = hash(key) % self.initial_capacity
        bucket = self.hash_table[hashKey]
        found = False

        for index,record in enumerate(bucket):
            recordKey, recordValue = record
            if recordKey == key:
                found = True
                break

        if found:
            bucket[index] = (key,value)
        else:
            bucket.append((key,value))

    def getValue(self,key):
        hashKey = hash(key) % self.initial_capacity
        bucket = self.hash_table[hashKey]
        found = False

        for index, record in enumerate(bucket):
            recordKey, recordValue = record
            if recordKey == key:
                found = True
                break
        if found:
            return recordValue
        else:
            return None

    def removeValue(self,key):
        hashKey = hash(key) % self.initial_capacity
        bucket = self.hash_table[hashKey]
        found = False

        for index, record in enumerate(bucket):
            recordKey, recordValue = record

            if recordKey == key:
                found = True
                break
            if found:
                bucket.pop(index)
            return

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)



print(table)

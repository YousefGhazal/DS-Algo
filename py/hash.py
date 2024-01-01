print("i'm hereeeee")


class HashTable:
    def __init__(self, m):
        self.m = m
        self.table = [None] * m

    def hash(self, k):
        return k % self.m

    def add(self, key, value):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.m
        self.table[index] = (key, value)

    def exists(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return True
            index = (index + 1) % self.m
        return False

    def get(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.m
        return None

    def remove(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return 
            index = (index + 1) % self.m

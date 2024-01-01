class Vector:
    def __init__(self):
        self.size = 0
        self.capacity = 16
        self.data = [None] * self.capacity

    def push_back(self, value):
        if self.size == self.capacity:
            self.capacity *= 2
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
            self.data = new_data
        self.data[self.size] = value
        self.size += 1

    def __getitem__(self, index):
        return self.data[index]

    def getSize(self):
        return self.size

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        print(f"self.storage[0] bd : {self.storage[0]}")
        del self.storage[0]
        print(f"self.storage[0] ad : {self.storage[0]}")
        print(f"self.storage bi : {self.storage}")
        self.storage.append(item)
        print(f"self.storage ai : {self.storage}")

    def get(self):
        pass


rb1 = RingBuffer(5)

rb1.append(1)
# rb1.append(2)
# rb1.append(3)

print(f"rb1 : {rb1}")

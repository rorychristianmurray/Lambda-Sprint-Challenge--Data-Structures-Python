class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):

        # print(f"self.storage[0] bd : {self.storage[0]}")
        del self.storage[0]
        # print(f"self.storage[0] ad : {self.storage[0]}")
        # print(f"self.storage bi : {self.storage}")
        self.storage.append(item)
        # print(f"self.storage ai : {self.storage}")

    def get(self):
        temp = []
        for i in self.storage:
            if i is not None:
                temp.append(i)
        return temp


rb1 = RingBuffer(5)

rb1.append('a')
rb1.append('b')
rb1.append('c')
rb1.append('d')
print(len(rb1.storage))
# len(rb1.storage)
print("\n\n")
print(rb1.get())
print("\n\n")
rb1.append('e')
print("\n\n")
print("\nlen(rb1.storage)\n")
print(len(rb1.storage))
print("\n\n")
print("\nrb1.get()\n")
print(rb1.get())
print("\nrb1.append('f')\n")
print(rb1.append('f'))
print("\nlen(rb1.storage)\n")
print(len(rb1.storage))
print("\nrb1.get()\n")
print(rb1.get())

# print(f"rb1 : {rb1}")

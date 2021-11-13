class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def size1(self):
        return self.size


q = ListQueue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue('True')
a = q.size1()
print(a)
print(q.dequeue())

class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []
        self.size = 0

    def is_empty(self):
        return self.inbound_stack == [] and self.outbound_stack == []

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        self.size -= 1
        return self.outbound_stack.pop()

    def enqueue(self, data):
        self.size += 1
        self.inbound_stack.append(data)

    def size1(self):
        return self.size


queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
print(queue.inbound_stack)
queue.dequeue()
print(queue.inbound_stack)
print(queue.outbound_stack)
queue.dequeue()
print(queue.outbound_stack)

# import sys


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def clear(self):
        self.tail = None
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.tail.next = self.head
        self.size += 1

    def delete(self, data):
        current = self.head
        prev = self.head
        while prev == current or prev != self.head:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


words = CircularList()
words.append('eggs')
words.append('ham')
words.append('spam')
counter = 0
for word in words.iter():
    print(word)
    counter += 1
    if counter > 1000:
        break
# sys.exit()


l = CircularList()
l.append('foo')
l.append('bar')
l.append('bim')
l.append('baz')
l.append('quux')
l.append('duux')
counter = 0
for item in l.iter():
    print(item)
    counter += 1
    if counter > 1000:
        break


print("Done iterating. Now we try to delete something that isn't there.")
l.delete('socks')
print('back to iterating')
counter = 0
for item in l.iter():
    print(item)
    counter += 1
    if counter > 1000:
        break


print('Let us delete something that is there.')
l.delete('foo')
print('back to iterating')
counter = 0
for item in l.iter():
    print(item)
    counter += 1
    if counter > 1000:
        break

class Node:
    def __init__(self, x):
        self.x = x
        self.next = None


s = SingleStack.from_list([1,2,3,4])
s2 = SingleStack.from_dict_values({...})

s3 = SingleStack()

class SingleStack:
    """invariant: at any point head contains an element to pop, tail contains last added element, n contains a number of elements"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def new_node(self, x):
        return Node(x)

    def push(self, x):
        u = self.new_node(x)
        if self.n == 0:
            self.tail = u
        u.next = self.head
        self.head = u
        self.n += 1

    def pop(self):
        if self.n == 0:
            return None
        x = self.head
        self.head = self.head.next
        self.n = self.n - 1
        if self.n == 0:
            self.tail = None
        return x.x

    def remove(self):
        return self.pop()

    def add(self, x):
        u = self.new_node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n = self.n + 1

    def show_tail(self):
        return self.tail.x

    def size(self):
        return self.n

    def get(self, i):
        if i < 0 or i > self.n-1:
            raise IndexError
        u = self.head
        for j in range(i):
            u = u.next
        return u.x

    def add_position(self, i, x):
        if i < 0 or i > self.n:
            raise IndexError
        if i == self.n:
            self.add(x)
        if i == 0:
            self.push(x)
        u = self.head
        for j in range(i-1):
            u = u.next
        w = self.new_node(x)
        w.next = u.next
        u.next = w
        self.n += 1


























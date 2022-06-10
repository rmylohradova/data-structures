class Linked_list:

    class Node:
        def __init__(self, x):
            self.x = x
            self.next = None

    def __init__(self):
        self.n = 0
        self.head = None
        self.tail = None

    def new_node(self, x):
        return Linked_list.Node(x)

    def add(self, x):
        u = self.new_node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1
        return True

    def push(self, x):
        u = self.new_node(x)
        u.next = self.head
        self.head = u
        if self.n == 0:
            self.tail = u
        self.n += 1

    def pop(self):
        if self.n == 0:
            return False
        x = self.head.x
        self.head = self.head.next
        self.n = self.n - 1
        if self.n == 0:
            self.tail = None
        return x

    def remove(self):
        self.pop()

    def size(self):
        return self.n

    def get(self, i):
        if i < 0 or i > self.n-1:
            return False
        u = self.head
        for j in range(i):
            u = u.next
        return u.x

    def set(self, i, x):
        y = self.get(i)
        y = x
        return y









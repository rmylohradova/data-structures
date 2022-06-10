class Node:
    def __init__(self, x):
        self.x = x
        self.next = None

class SLlist:
    def __init__(self):
        self.n = 0
        self.head = None
        self.tail = None

    def new_node(self, x):
        return Node(x)

    def add(self, x):
        u = self.new_node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1
        return True

    def remove(self):
        self.pop()

    def push(self,x):
        u = self.new_node(x)
        u.next = self.head
        self.head = u
        if self.n == 0:
            self.tail = u
        self.n += 1

    def pop(self):
        if self.n == 0:
            return None
        x = self.head.x
        self.head = self.head.next
        self.n = self.n - 1
        if self.n == 0:
            self.tail = None
        return x

    def size(self):
        return self.n

    def printList(self):
        temp = self.head
        while temp:
            print(temp.x)
            temp = temp.next

    def get(self, i):
        if i < 0 or i > self.n-1:
            return False
        u = self.head
        for j in range(i):
            u = u.next
        return u.x

    def set(self, i, x):
        if i < 0 or i > self.n - 1:
            return False
        u = self.head
        for j in range(i):
            u = u.next
        u.x = x
        return u.x

    def remove_position(self, i):
        if i < 0 or i > self.n - 1:
            return False
        if i == 0:
            self.pop()
        u = self.head
        for j in range(i-1):
            u = u.next
        w = u.next
        u.next = u.next.next
        return w

    def add_position(self, i, x):
        if i < 0 or i > self.n:
            return False
        if i == 0:
            self.push(x)
        u = self.head
        for j in range(i-1):
            u = u.next
        w = self.new_node(x)
        w.next = u.next
        u.next = w
        self.n += 1
        return w

    def second_last(self):
        y = self.head
        if y is None or y.next is None:
            return False
        while y is not None:
            if y.next.next is None:
                return y.x
            y = y.next














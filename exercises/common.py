import random
class Input:

    def __init__(self, elements):
        self.elements = elements
        self.index = 0

    def next(self):
        if self.index >= len(self.elements):
            return None

        element = self.elements[self.index]
        self.index = self.index + 1
        return element


class Output:

    def __init__(self):
        self.storage = []

    def out(self, element):
        self.storage.append(element)

    def result(self):
        return self.storage


class Stack:

    def __init__(self):
        self.storage = []

    def push(self, x):
        self.storage.append(x)

    def pop(self):
        return self.storage.pop()

    def size(self):
        return len(self.storage)


class Queue:

    def __init__(self):
        self.storage = []

    def add(self, x):
        self.storage.append(x)

    def remove(self):
        return self.storage.pop(0)

    def size(self):
        return len(self.storage)


class MyList:

    def __init__(self, elements):
        self.elements = elements

    def size(self):  # return the size of the list
        return len(self.elements)

    def get(self, i):  # return the element x index i
        return self.elements[i]

    def set(self, i, x):  # set the value of element [i] to x
        self.elements[i] = x
        return self.elements

    def add(self, i, x):  # add x at the position of i
        self.elements.insert(i, x)
        return self.elements

    def remove(self, i):  # remove the value of x index i
        self.elements.pop(i)
        return self.elements



class ArrayQueue:

    def __init__(self):
        self.a = [None]*5
        self.j = 0
        self.n = 0

    def size(self):
        return len(self.a)

    def count_number(self):
        return self.n

    def add(self, x):
        if self.n + 1 > len(self.a):
            self.resize()
        x = self.a[(self.n + self.j) % len(self.a)]
        self.n += 1
        return self.n

    def remove(self):
        if len(self.a) == 0:
            return False
        else:
            x = self.a[self.j]
            self.j = (self.j + 1) % len(self.a)
            self.n = self.n - 1
            if len(self.a) >= 3*self.n:
                self.resize()
            return x

    def rotate(self, r):
        r = r % len(self.a)
        i = 0
        count_rotated = 0
        while count_rotated < len(self.a):
            rotated_index = (i + r) % len(self.a)
            temp = self.a[rotated_index]
            self.a[rotated_index] = self.a[i]
            count_rotated += 1
            j = rotated_index
            while j != i and count_rotated < len(self.a):
                rotated_index = (j + r) % len(self.a)
                self.a[rotated_index], temp = temp, self.a[rotated_index]
                count_rotated += 1
                j = rotated_index
                print(self.a)
            i += 1
        return self.a

    def resize(self):
        b = [None]*2*self.n
        for k in range(self.n):
            b[k] = self.a[(self.j+k) % len(self.a)]
            self.a = b
            self.j = 0



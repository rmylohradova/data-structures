import random

class RandomQueue:

    def __init__(self):
        self.a = [0 for i in range(5)]
        self.n = 0

    def size(self):
        return len(self.a)

    def count_number(self):
        return self.n

    def add(self, x):
        if self.n + 1 > len(self.a):
            self.resize()
        x = self.a[self.n % len(self.a)]
        self.n += 1
        return self.n

    def remove(self):
        if len(self.a) == 0:
            return False
        else:
            random_index = random.randint(0, self.n-1)
            self.a[self.n-1], self.a[random_index] = self.a[random_index], self.a[self.n-1]
            self.n = self.n - 1
            if len(self.a) >= 3*self.n:
                self.resize()
            return self.a[self.n]

    def resize(self):
        b = [0 for i in range(2*self.n)]
        for k in range(self.n):
            b[k] = self.a[k % len(self.a)]
            self.a = b

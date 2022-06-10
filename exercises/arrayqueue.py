class ArrayQueue:
    def __init__(self):
        self.a = [None]*5
        self.j = 0
        self.n = 0

    def elements_count(self):
        return self.n

    def array_size(self):
        return len(self.a)

    def resize(self):
        b = [None] * 2 * self.n
        for k in range(self.n):
            b[k] = self.a[self.j+k % len(self.a)]
            self.a = b
            self.j = 0

    def add(self, x):
        if self.n + 1 > len(self.a):
            self.resize()
        x = (self.n + self.j) % len(self.a)
        self.n += 1
        return self.n

    def remove(self):
        if len(self.a) == 0:
            return False
        else:
            x = self.a[self.j]
            self.j = (self.j + 1)% len(self.a)
            self.n = self.n - 1
            if len(self.a) >= 3*self.n:
                self.resize()
        return x

    def rotate(self, r):
        r = r % len(self.a)
        d = r
        b = []
        while d != 0:
            b.append(self.a[len(a)-d])
            d = d-1
        i = 0
        for i in range(len(self.a)-r):
            b.append(self.a[i])
        self.a = d




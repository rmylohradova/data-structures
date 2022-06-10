from exercises.stack import SingleStack

def test1():
    a = SingleStack()
    a.push(1)
    assert a.size() == 1

def test2():
    a = SingleStack()
    a.push(1)
    a.push(2)
    a.pop()
    assert a.size() == 1

def test2():
    a = SingleStack()
    a.push(1)
    a.push(2)
    assert a.pop() == 2
    assert a.size() == 1

def test3():
    a = SingleStack()
    a.push(1)
    a.push(2)
    assert a.pop() == 2
    assert a.pop() == 1
    assert a.size() == 0

def test4():
    a = SingleStack()
    a.push(1)
    a.add(2)
    assert a.show_tail() == 2
    assert a.size() == 2

def test5():
    a = SingleStack()
    a.push(1)
    a.add(2)
    assert a.remove() == 1
    assert a.show_tail() == 2
    assert a.size() == 1

def test6():
    a = SingleStack()
    a.add(1)
    a.add(2)
    a.add(3)
    assert a.get(2) == 3
    assert a.get(0) == 1



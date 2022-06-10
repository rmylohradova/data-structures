from exercises.rotate_array import rotate, rotate_array, rotate_temp
from exercises.common import ArrayQueue


def test_rotate1():
    assert rotate_array([1, 2, 3, 4], 3) == [2, 3, 4, 1]


def test_rotate2():
    assert rotate_array([1,2,3,4], 2) == [3,4,1,2]


def test_rotate_temp():
    assert rotate_temp([1,2,3,4], 2) == [3,4,1,2]

def test_rotate_slice():
    assert rotate([1, 2, 3, 4], 2) == [3, 4, 1, 2]

def test_negative():
    assert rotate_array([1,2,3,4,5,6,7,8,9], -1) == [2,3,4,5,6,7,8,9,1]

def test_negative_temp():
    assert rotate_temp([1,2,3,4,5,6,7,8,9], -1) == [2,3,4,5,6,7,8,9,1]

def test_negative2():
    assert rotate_array([1,2,3,4,5,6,7,8,9], 68) == [5,6,7,8,9,1,2,3,4]

def test_array_rotate():
    a = ArrayQueue()
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    a.add(5)
    assert a.rotate(2) == [4,5,1,2,3]

def test_array():
    a = ArrayQueue()
    a.add(1)
    a.add(2)
    assert a.size() == 5

def test_array_growing():
    a = ArrayQueue()
    for i in range(11):
        a.add(i)
    assert a.size() == 20


def test_array_shrinking():
    a = ArrayQueue()
    for i in range(6):
        a.add(i)
    for i in range(4):
        a.remove()
    assert a.size() == 4





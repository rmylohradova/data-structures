from exercises.common import MyList


def test_list():
    l = MyList([1,2,3])
    assert l.size() == 3

def test_list_get():
    l = MyList([1, 2, 3, 4,5,6,7,8])
    assert l.get(-1) == 8

def test_list_remove():
    l = MyList([1, 2, 3, 4,5,6,7,8])
    assert l.remove(-1) == [1,2,3,4,5,6,7]

def test_list_add():
    l = MyList([1, 2, 3, 4,5,6,7,8])
    assert l.add(1, 10) == [1,10,2,3,4,5,6,7,8]

def test_list_set():
    l = MyList([1, 2, 3, 4,5,6,7,8])
    assert l.set(1, 1) == [1,1,3,4,5,6,7,8]


def isDyckword(input):
    check = 0
    for index, element in enumerate(input):
        check = check + element
        if check < 0:
            print(check)
            return False
    if check >= 0:
        print(check)
        return True



def test_dyckword():
    input = [1, -1, 1, -1, 1,1,1,1,1,]
    assert isDyckword(input) == True


def test_dyckword3():
    input = [-1, -1, -1, -1, -1,-1,1]
    assert isDyckword(input) == False


def test_dyckword3():
    input = [-1,-1,1,1,1,1,1,1,1]
    assert isDyckword(input) == False

def test_dyckwordnot():
    input = [1, -1, 1, -1, -1,-1,-1,-1,-1]
    assert isDyckword(input) == False


def test_dyckword0():
    input = [1, -1, 1, -1]
    assert isDyckword(input) == True


def test_dyckword9():
    input = [-1, 1, -1, 1]
    assert isDyckword(input) == False
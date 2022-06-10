from exercises.common import Stack, Input, Output


def solution(input, output, limit):
    stack = Stack()
    while True:
        element = input.next()
        if element is None:
            while stack.size() != 0:
                output.out(stack.pop())
            break
        if stack.size() != limit:
            stack.push(element)
        if stack.size() == limit:
            while stack.size() != 0:
                output.out(stack.pop())




def  test_exact_fit():
    input = Input([1,2,3,4,5,6])
    output = Output()

    solution(input, output, 3)

    assert output.result() == [3,2,1,6,5,4]


def test_not_exact_fit():
    input = Input([1,2,3,4,5])
    output = Output()

    solution(input, output, 3)

    assert output.result() == [3,2,1,5,4]


def test_not_exact_fit2():
    input = Input([1,2,3,4,5,6,7])
    output = Output()

    solution(input, output, 3)

    assert output.result() == [3,2,1,6,5,4,7]


def test_one_element():
    input = Input([1])
    output = Output()

    solution(input, output, 3)

    assert output.result() == [1]


def test_two_elements():
    input = Input([1,2])
    output = Output()

    solution(input, output, 3)

    assert output.result() == [2,1]

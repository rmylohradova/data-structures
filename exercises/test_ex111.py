from exercises.common import Stack, Input, Output


def solution(input, output):
    stack = Stack()
    while True:
        element = input.next()
        if element is None:
            break
        stack.push(element)
    while stack.size() != 0:
        output.out(stack.pop())


def test_simple():
    input = Input([1,2,3,4,5])
    output = Output()

    solution(input, output)

    assert output.result() == [5,4,3,2,1]


def test_simple2():
    input = Input([1])
    output = Output()

    solution(input, output)

    assert output.result() == [1]

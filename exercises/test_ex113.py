from exercises.common import Input, Output, Queue


def solution(input, output, return_step):
    queue = Queue()
    while True:
        element = input.next()
        if element is None:
            break
        if queue.size() <= return_step:
            queue.add(element)
        if queue.size() == return_step+1:
            if element == 0:
                output.out(queue.remove())
            else:
                queue.remove()


def solution_simple_queue(input, output):
    queue = Queue()
    while True:
        element = input.next()
        if element is None:
            break
        queue.add(element)
    while queue.size() != 0:
        a = queue.remove()
        output.out(a)



def test_queue():
    input = Input([1,2,3,4,5,6,7,8])
    output = Output()
    solution_simple_queue(input, output)
    assert output.result() == [1,2,3,4,5,6,7,8]


def test_one_missing_element():
    input = Input([1,2,3,4,5,6,7,8,0,9])
    output = Output()

    solution(input, output, 7)

    assert output.result() == [2]


def test_2_missing_elements():
    input = Input([1,2,3,4,0,0,7,8,2,9])
    output = Output()

    solution(input, output, 3)

    assert output.result() == [2,3]

def test_first_missing():
    input = Input([1,2,3,0])
    output = Output()

    solution(input, output, 3)

    assert output.result() == [1]


def test_last2_missing():
    input = Input([1,2,3,4,5,6,7,8,9,0,0,3,0])
    output = Output()

    solution(input, output, 3)

    assert output.result() == [7, 8, 0]


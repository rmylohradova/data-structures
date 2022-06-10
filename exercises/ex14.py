from exercises.common import Stack, Queue, Input, Output

def reverse_stack(input, output):
    s = Stack()
    q = Queue()
    while True:
        element = input.next()
        print(element)
        if element is None:
            break
        s.push(element)
    while s.size() != 0:
        item = s.pop()
        q.add(item)
    while q.size() != 0:
        a = q.remove()
        print(a)
        output.out(a)
        s.push(a)



def test_simple():
    input = Input([1,2,3,4,5])
    output = Output()

    reverse_stack(input, output)

    assert output.result() == [5,4,3,2,1]






from exercises.common import Stack

m = {
    ')': '(',
    '}': '{',
    ']': '[',
}

def matched_string(string):
    stack = Stack()
    pairs_count = 0
    for char in string:
        print(char)
        if char == '{' or char == '[' or char == '(':
            stack.push(char)
        if char == '}' or char == ')' or char == ']':
            if stack.size() == 0:
                return False
            last_char = stack.pop()
            if m[char] != last_char:
                # pairs_count += 1
                return False
            print(last_char)
            # if char == '}' and last_char == '{' or char == ')' and last_char == '(' or char == ']' and last_char == '[':
            #     pairs_count += 1
    return True
    # if pairs_count == len(string)/2:
    #     return True
    # else:
    #     return False



def test1():
    string = "{{()[]}}"
    assert matched_string(string) == True

def test2():
    string = "{{()]}"
    assert matched_string(string) == False

def test3():
    string = "{{{)]}"
    assert matched_string(string) == False

def test4():
    string = "}{{)]}"
    assert matched_string(string) == False

def test6():
    string = "{}"
    assert matched_string(string) == True

def test7():
    string = "({})"
    assert matched_string(string) == True

def test8():
    string = "((])"
    assert matched_string(string) == False

def test9():
    string = "(([]))"
    assert matched_string(string) == True

def test9():
    string = "(([)])"
    assert matched_string(string) == False

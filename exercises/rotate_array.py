
def rotate_array(a, r):
    r = r % len(a)
    i = 0
    count_rotated = 0
    while count_rotated < len(a):
        rotated_index = (i + r) % len(a)
        temp = a[rotated_index]
        a[rotated_index] = a[i]
        count_rotated += 1
        j = rotated_index
        while j != i and count_rotated < len(a):
            rotated_index = (j + r) % len(a)
            a[rotated_index], temp = temp, a[rotated_index]
            count_rotated += 1
            j = rotated_index
            print(a)
        i += 1
    return a


def rotate_temp(a, r):
    r = r % len(a)
    p = r
    b = []
    while p != 0:
        b.append(a[len(a)-p])
        p = p - 1
    print(b)
    i = 0
    for i in range(len(a)-r):
        b.append(a[i])
    print(b)
    return b



def rotate(a, r):
    r = r % len(a)
    return a[-r:] + a[:-r]

# array = [1,2,3,4,5]
# print(array)
# reversed = array[::-1]
#
# first_two_reversed = reversed[1::-1]
#
# last_reversed = reversed[:-4:-1]
#
# rotated = first_two_reversed+last_reversed
# print(rotated)


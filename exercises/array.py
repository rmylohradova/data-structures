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

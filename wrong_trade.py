a = [1, 2, 3, 4, 5]


def correct_max_aij(a):
    current_value = 0
    current_ans = (None, None)

    b = [0]
    for i in range(0, len(a)):
        new_b = b[i] + a[i]
        b.append(new_b)
    print(b)

correct_max_aij(a)

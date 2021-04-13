a = [1,2,3,4,5]


def correct_max_aij(a):
    current_value = 0
    current_ans = (None, None)

    b = [0]
    for i in range(0, len(a)):
        new_b = b[i] + a[i]
        b.append(new_b)
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            aux = b[j+1]-b[i]
            if aux > current_value:
                current_value = aux
                current_ans = (i, j)
    
    print(current_ans)
    print(current_value)



def wrong_max_aij(a):
    current_value = 0
    current_ans = (None, None)

    b = [a[0]]
    for i in range(1, len(a)):
        new_b = b[i-1] + a[i]
        b.append(new_b)

    print(b)

    min_i_value = b[0]
    min_i = 0

    for i in range(0, len(a)):
        if b[i] < min_i:
            min_i_value = b[i]
            min_i = i
    # print()
    # print(min_i)
    # print(min_i_value)
    # print()
    max_j_value = b[min_i]
    max_j = min_i
    
    for j in range(min_i, len(a)):
        print(j)
        print(b[j])
        print()
        if b[j] > max_j:
            max_j_value = b[j]
            max_j = j
    
    current_ans = (min_i, max_j-1)
    current_value = b[max_j-1]-b[min_i]

    print(current_ans)
    print(current_value)

correct_max_aij(a)
wrong_max_aij(a)
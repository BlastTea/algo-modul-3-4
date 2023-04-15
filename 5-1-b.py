def find_it(A, k):
    len_arr = len(A)

    if len_arr == 1:
        if A[0] == k:
            return 1
        return 0

    mid = len_arr // 2
    m1 = find_it(A[0:mid], k)
    m2 = find_it(A[mid:len_arr], k)

    return m1 + m2


A = [3, 1, 6, 3, 9, -10]
print(find_it(A, 3))
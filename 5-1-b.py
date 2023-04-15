def find_it(arr, k):
    len_arr = len(arr)

    if len_arr == 1:
        if arr[0] == k:
            return 1
        return 0

    mid = len_arr // 2
    m1 = find_it(arr[0:mid], k)
    m2 = find_it(arr[mid:len_arr], k)

    return m1 + m2


arr = [3, 1, 6, 3, 9, -10]
print(find_it(arr, 3))
def find_it(A, start, end):
    if start == end:
        return 0
    else:
        mid = (start + end) // 2

        left_max_diff = find_it(A, start, mid)
        right_max_diff = find_it(A, mid + 1, end)

        left_max = -float('inf')
        right_min = float('inf')
        for i in range(start, mid + 1):
            if A[i] > left_max:
                left_max = A[i]
        for i in range(mid + 1, end + 1):
            if A[i] < right_min:
                right_min = A[i]
        mid_max_diff = left_max - right_min

        return max(left_max_diff, right_max_diff, mid_max_diff)


A = [12, 1, 1, 2, 5, 7, 6, 9, 14]
print(find_it(A, 0, len(A) - 1))
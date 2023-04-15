def find_it(A):
    diff = 0
    for i in range(len(A) - 1):
        diff = max(diff, abs(A[i] - A[i + 1]))
    return  diff


A = [12, 1, 1, 2, 5, 7, 6, 9, 14]
print(find_it(A))
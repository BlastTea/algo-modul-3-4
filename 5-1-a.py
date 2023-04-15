def find_it(A, k):
    count = 0
    for i in A:
        if i == k : count += 1
    return count

A = [3, 1, 6, 3, 9, -10]
print(find_it(A, 3))
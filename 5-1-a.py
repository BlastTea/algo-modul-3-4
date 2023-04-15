def find_it(arr, k):
    count = 0
    for i in arr:
        if i == k : count += 1
    return count

arr = [3, 1, 6, 3, 9, -10]
print(find_it(arr, 3))
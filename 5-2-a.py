def find_it(arr):
    diff = 0
    for i in range(len(arr) - 1):
        diff = max(diff, abs(arr[i] - arr[i + 1]))
    return  diff


arr = [12, 1, 1, 2, 5, 7, 6, 9, 14]
print(find_it(arr))
def binary_search(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] == value:
            return left
        if arr[right] == value:
            return right
        
        mid = left + int(((value - arr[left]) * (right - left)) / (arr[right] - arr[left]))
        
        if arr[mid] == value:
            return mid
        
        if value < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
        
    return -1

print(f'9000 berada pada index {binary_search([i for i in range(100, 10001)], 9000)}')

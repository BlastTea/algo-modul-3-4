import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def visualize_merge_sort(arr):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(arr)), arr)
    plt.title('Merge Sort')
    plt.show(block=False)
    plt.pause(1)

    sorted_arr = merge_sort(arr)

    plt.clf()
    plt.bar(range(len(sorted_arr)), sorted_arr)
    plt.title('Merge Sort - Sorted Array')
    plt.show()

arr = [3, 12, 1, 10, 27, 11, 5, 2, 87, 17, 9]
visualize_merge_sort(arr)
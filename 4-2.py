def mencari_selisih(arr, k):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == k:
                print(f'{arr[i]} - {arr[j]} = {k}')

mencari_selisih([1, 2, 2, 5, 9, 13, 14, 17], 3)

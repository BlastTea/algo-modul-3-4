def find_it(arr):
    len_arr = len(arr)

    if len_arr == 1:
        return arr[0]

    mid = len_arr // 2
    m1 = find_it(arr[0:mid])
    m2 = find_it(arr[mid:len_arr])

    return m1 + m2


arr = [12, 1, 1, 2, 5, 7, 6, 9, 14]
result = find_it(arr)
print(f'Selisih terbesar antara dua bilangan berurutan di A adalah {result[2]} antara bilangan {result[0]} dan {result[1]}')
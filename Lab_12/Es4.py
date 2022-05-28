
def merge_sort_rec(array, n=2):
    n = n
    for i in range(0, len(array), n):
        print(array[i:i + n])
        for j in range(i+1, i+n-1):
            if array[j+1] < array[j]:
                array[j], array[j+1] = array[j+1], array[j]
        print(array[i:i+n])
    if n <= len(array)//2:
        merge_sort_rec(array, n*2)


# array = [5, 2, 4, 9, 45, 26, 32, 1, 6, 15, 8, 22, 12, 25]
array = [23, 12, 1, 134, 6, 13, 45, 0]

print(array)

merge_sort_rec(array)


def merge_sort_rec(array, n=2):
    n = n
    for i in range(0, len(array) - n, n):  # Sezioni di n-elementi della lista
        j = i+n
        while j > i:  # Ordino gli elementi nelle sezioni
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
                if j < len(array) - 1:
                    j += 1
            else:
                j -= 1
    if n <= len(array)//2:
        merge_sort_rec(array, n*2)


array = [5, 2, 4, 9, 45, 26, 32, 1, 6, 15, 8, 22, 12, 25]
array2 = [23, 12, 1, 134, 6, 13, 45, 0]


print(array)
merge_sort_rec(array)
print(array)

print()

print(array2)
merge_sort_rec(array2)
print(array2)


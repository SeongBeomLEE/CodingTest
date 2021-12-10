import random
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    l_arr = merge_sort(left)
    r_arr = merge_sort(right)
    i, j = 0, 0
    result = []
    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] < r_arr[j]:
            result.append(l_arr[i])
            i += 1
        else:
            result.append(r_arr[j])
            j += 1
    result += l_arr[i:]
    result += r_arr[j:]
    return result

arr = [i for i in range(1, 100)]
random.shuffle(arr)
print(arr)
print(merge_sort(arr = arr))
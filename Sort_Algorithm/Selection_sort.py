import random
def selection_sort(arr):
    for idx in range(0, len(arr) - 1):
        min_value_idx = idx
        for next_idx in range(idx + 1, len(arr)):
            if arr[next_idx] < arr[min_value_idx]:
                min_value_idx = next_idx
        tmp = arr[min_value_idx]
        arr[min_value_idx] = arr[idx]
        arr[idx] = tmp
    return arr

arr = [i for i in range(1, 100)]
random.shuffle(arr)
print(arr)
print(selection_sort(arr = arr))
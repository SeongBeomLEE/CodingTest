import random
def insertion_sort(arr):
    for idx in range(1, len(arr)):
        current_value = arr[idx]
        position = idx
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
    return arr

arr = [i for i in range(1, 100)]
random.shuffle(arr)
print(arr)
print(insertion_sort(arr = arr))
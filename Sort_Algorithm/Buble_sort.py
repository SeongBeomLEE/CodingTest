import random
def buble_sort(arr):
    for loop in range(len(arr) - 1, 0, -1):
        for idx in range(loop):
            if arr[idx] > arr[idx + 1]:
                tmp = arr[idx]
                arr[idx] = arr[idx + 1]
                arr[idx + 1] = tmp
    return arr

arr = [i for i in range(1, 100)]
random.shuffle(arr)
print(arr)
print(buble_sort(arr = arr))
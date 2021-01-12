# 부품 찾기
# N = int(input())
# array1 = list(map(int, input().split()))
# M = int(input())
# array2 = list(map(int, input().split()))

N = 5
array1 = [8, 3, 7, 9, 2]
M = 3
array2 = [5, 7, 9]

array1.sort()

def binary_sort(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target: return True
        elif array[mid] < target: start = mid + 1
        else: end = mid - 1

    return False

for i in array2:
    if binary_sort(array1, i, 0, N - 1): print('yes', end=" ")
    else: print('no', end=" ")

# 숫자 카드 2
import sys

N = int(sys.stdin.readline().rstrip())
# 가지고 았는 카드
array1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
# 찾을 카드
array2 = list(map(int, sys.stdin.readline().split()))
array1.sort()


def binary_sort(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target: return array[start:end+1].count(target)
        elif array[mid] < target: start = mid + 1
        else: end = mid - 1

    return 0

n_dic = {}
for n in array1:
    start = 0
    end = N - 1
    if n not in n_dic:
        n_dic[n] = binary_sort(array1, n, start, end)

print(" ".join([str(n_dic[x]) if x in n_dic else '0' for x in array2]))
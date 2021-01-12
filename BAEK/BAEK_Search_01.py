# 수 찾기
# 핵심 아이디어
# 이진 탐색을 활용한다.
# N = 5
# A = [4, 1, 5, 2, 3]
# M = 5
# in_A = [1, 3, 7, 9, 5]

N = int(input())
A = list(map(int, input().split()))
M = int(input())
in_A = list(map(int, input().split()))

A.sort()
def bibary_serch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target: return 1
        elif array[mid] < target: start = mid + 1
        else: end = mid - 1

    return 0

for i in in_A:
    print(bibary_serch(A, i, 0, N-1))
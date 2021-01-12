# 나무자르기
# 해답을 함수화 시키면 시간초과 오류가 해결됨

# N, M = 4, 7
# array = [20, 15, 10, 17]

import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

def solution():
    start, end = 1, max(array)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in array:
            if i > mid : total += i - mid
        if total >= M :
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

print(solution())
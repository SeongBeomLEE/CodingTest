# https://www.acmicpc.net/problem/15656
# N과 M (7)
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

values = list(map(str, sorted(list(map(int, input().rstrip().split(" "))))))

def solution(answer, m):
    if m == M: print(" ".join(answer))
    if m < M:
        for idx in range(N):
            solution(answer + [values[idx]], m + 1)

for idx in range(N):
    solution([values[idx]], 1)
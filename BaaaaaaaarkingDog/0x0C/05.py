# https://www.acmicpc.net/problem/15651
# N과 M (3)
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

values = [str(i) for i in range(1, N + 1)]

def solution(answer, m):
    if m == M: print(" ".join(answer))
    if m < M:
        for idx in range(N):
            solution(answer + [values[idx]], m + 1)

for idx in range(N):
    solution([values[idx]], 1)
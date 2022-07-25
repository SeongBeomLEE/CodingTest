# https://www.acmicpc.net/problem/15652
# N과 M (4)
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

values = [str(i) for i in range(1, N + 1)]

def solution(answer, start_idx, m):
    if m == M: print(" ".join(answer))
    if m < M:
        for idx in range(start_idx, N):
            solution(answer + [values[idx]], idx, m + 1)

for idx in range(N):
    solution([values[idx]], idx, 1)
# https://www.acmicpc.net/problem/15650
# N과 M (2)
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

values = [str(i) for i in range(1, N + 1)]

def solution(answer, start_idx, m):
    if m == M: print(" ".join(answer))
    for idx in range(start_idx, N):
        solution(answer + [values[idx]], idx + 1, m + 1)

for idx in range(N):
    solution([values[idx]], idx + 1, 1)
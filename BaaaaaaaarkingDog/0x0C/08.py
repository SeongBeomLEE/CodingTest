# https://www.acmicpc.net/problem/1565
# N과 M (6)
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

values = list(map(str, sorted(list(map(int, input().rstrip().split(" "))))))

def solution(answer, start_idx, m):
    if m == M: print(" ".join(answer))
    if m < M:
        for idx in range(start_idx, N):
            solution(answer + [values[idx]], idx + 1, m + 1)

for idx in range(N):
    solution([values[idx]], idx + 1, 1)
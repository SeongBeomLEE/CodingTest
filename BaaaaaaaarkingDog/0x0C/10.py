# https://www.acmicpc.net/problem/15657
# N과 M (8)
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

values = list(map(str, sorted(list(map(int, input().rstrip().split(" "))))))

def solution(answer, strat_idx, m):
    if m == M: print(" ".join(answer))
    if m < M:
        for idx in range(strat_idx, N):
            solution(answer + [values[idx]], idx, m + 1)

for idx in range(N):
    solution([values[idx]], idx, 1)
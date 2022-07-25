# https://www.acmicpc.net/problem/15664
# N과 M (10)
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

values = list(map(str, sorted(list(map(int, input().rstrip().split(" "))))))
check = {}

def solution(answer, start_idx, m):
    if m == M: 
        answer = " ".join(answer)
        if answer not in check:
            check[answer] = True
            print(answer)
    if m < M:
        for idx in range(start_idx, N):
            solution(answer + [values[idx]], idx + 1, m + 1)

for idx in range(N):
    solution([values[idx]], idx + 1, 1)
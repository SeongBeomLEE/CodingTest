# https://www.acmicpc.net/problem/15665
# N과 M (11)
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

values = list(map(str, sorted(list(map(int, input().rstrip().split(" "))))))
check = {}

def solution(answer, m):
    if m == M: 
        answer = " ".join(answer)
        if answer not in check:
            check[answer] = True
            print(answer)
    if m < M:
        for idx in range(N):
            solution(answer + [values[idx]], m + 1)

for idx in range(N):
    solution([values[idx]], 1)
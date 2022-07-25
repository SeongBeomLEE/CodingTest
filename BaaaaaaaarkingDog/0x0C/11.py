# https://www.acmicpc.net/problem/15663
# N과 M (9)
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

values = list(map(str, sorted(list(map(int, input().rstrip().split(" "))))))
check = {}

def solution(answer, visit, m):
    if m == M: 
        answer = " ".join(answer)
        if answer not in check:
            check[answer] = True
            print(answer)
    if m < M:
        for idx in range(N):
            if not visit[idx]:
                visit[idx] = True
                solution(answer + [values[idx]], visit, m + 1)
                visit[idx] = False

visit = [False] * N
for idx in range(N):
    visit[idx] = True
    solution([values[idx]], visit, 1)
    visit[idx] = False
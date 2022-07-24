# https://www.acmicpc.net/problem/15649
# N과 M (1)
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().rstrip().split(" "))

# values = [str(i) for i in range(1, N + 1)]

# def solution(answer, m):
#     if m == M: print(" ".join(answer))
#     for i in values:
#         if i not in answer:
#             solution(answer + [i], m + 1)

# for i in values:
#     solution([i], 1)

'''

방문 여부 list를 이용한 풀이

answer에서 탐색보다 O(1)의 검색으로 더욱더 빠르게 백트래킹

'''

import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(" "))

values = [str(i) for i in range(1, N + 1)]

def solution(answer, visit, m):
    if m == M: print(" ".join(answer))
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
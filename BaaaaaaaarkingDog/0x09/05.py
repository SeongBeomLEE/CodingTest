# https://www.acmicpc.net/problem/1697
# 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().rstrip().split(" "))
visit = [False] * 100001

answer = 0
match = False
q = deque([N])
visit[N] = True

while q:
    for _ in range(len(q)):
        n = q.popleft()
        if n == K:
            match = True
            break
        for i in range(3):
            if i == 0:
                dn = n * 2
                if dn <= 100000 and not visit[dn]:
                    visit[dn] = True
                    q.append(dn)
            elif i == 1:
                dn = n + 1
                if dn <= 100000 and not visit[dn]:
                    visit[dn] = True
                    q.append(dn)
            elif i == 2:
                dn = n - 1
                if 0 <= dn and not visit[dn]:
                    visit[dn] = True
                    q.append(dn)

    if match: break
    answer += 1

if match:
    print(answer)
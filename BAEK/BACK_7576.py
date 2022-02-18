# 토마토
from collections import deque

M, N = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

q = deque([])
for n in range(N):
    for m in range(M):
        if arr[n][m] == 1:
            q.append([n, m])

answer = 0

dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

while q:
    n, m = q.popleft()
    for i in range(4):
        nn, nm = n + dn[i], m + dm[i]
        if 0 <= nn < N and 0 <= nm < M and arr[nn][nm] == 0:
            arr[nn][nm] = arr[n][m] + 1
            q.append([nn, nm])

tmp = False
for ii in arr:
    for i in ii:
        if i == 0:
            answer = 0
            tmp = True
            break
        answer = max(answer, i)
    if tmp: break

print(answer - 1)



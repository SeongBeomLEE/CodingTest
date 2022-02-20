# 미로탐색
from collections import deque

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, list(input()))))

q = deque([[0, 0]])
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if arr[ny][nx] != 0:
                if arr[ny][nx] == 1:
                    arr[ny][nx] = arr[y][x] + 1
                    q.append([nx, ny])

print(arr[N-1][M-1])
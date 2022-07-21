# https://www.acmicpc.net/problem/2178
# 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().rstrip().split(" "))
maps = []
for _ in range(n):
    rows = list(map(int, list(input().rstrip())))
    maps.append(rows)

visits = [[False for _ in range(m)] for _ in range(n)]

for row in range(n):
    for col in range(m):
        if maps[row][col] == 0:
            visits[row][col] = True

q = deque([(0, 0)])
visits[0][0] = True
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    row, col = q.popleft()
    now_length = maps[row][col]
    for i in range(4):
        x, y = dx[i], dy[i]
        if 0 <= (col + x) and (col + x) < m and 0 <= (row + y) and (row + y) < n:
            if not visits[row + y][col + x]:
                maps[row + y][col + x] = now_length + 1
                visits[row + y][col + x] = True
                q.append((row + y, col + x))

print(maps[-1][-1])



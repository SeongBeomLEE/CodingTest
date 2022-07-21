# https://www.acmicpc.net/problem/1926
# 그림
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().rstrip().split(" "))
maps = []
for _ in range(n):
    rows = list(map(int, input().rstrip().split(" ")))
    maps.append(rows)

starts = []
visits = [[True for _ in range(m)] for _ in range(n)]
for row in range(n):
    for col in range(m):
        if maps[row][col] == 1:
            starts.append((row, col))
            visits[row][col] = False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []
for row, col in starts:
    if not visits[row][col]:
        size = 0
        q = deque([(row, col)])
        visits[row][col] = True
        while q:
            row, col = q.popleft()
            size += 1
            for i in range(4):
                x, y = dx[i], dy[i]
                if 0 <= (col + x) and (col + x) < m and 0 <= (row + y) and (row + y) < n:
                    if not visits[row + y][col + x]:
                        q.append((row + y, col + x))
                        visits[row + y][col + x] = True
                        
        answer.append(size)

if answer:
    print(len(answer))
    print(max(answer))
else:
    print(0)
    print(0)



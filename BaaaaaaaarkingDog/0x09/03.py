# https://www.acmicpc.net/problem/7576
# 토마토
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().rstrip().split(" "))
maps = []
for _ in range(m):
    rows = list(map(int, input().rstrip().split(" ")))
    maps.append(rows)

starts = []

for row in range(m):
    for col in range(n):
        if maps[row][col] == 1:
            starts.append((row, col))

q = deque(starts)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    row, col = q.popleft()
    now_count = maps[row][col]
    for i in range(4):
        x, y = dx[i], dy[i]
        if 0 <= (col + x) and (col + x) < n and 0 <= (row + y) and (row + y) < m:
            if maps[row + y][col + x] == 0:
                maps[row + y][col + x] = now_count + 1
                q.append((row + y, col + x))

def show_answer(maps, n, m):
    max_count = 0
    for row in range(m):
        for col in range(n):
            if maps[row][col] == 0:
                return -1
            max_count = max(max_count, maps[row][col])
    
    return max_count - 1

print(show_answer(maps, n, m))



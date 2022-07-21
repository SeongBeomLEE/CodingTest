# https://www.acmicpc.net/problem/4179
# 불!
import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int, input().rstrip().split(" "))
maps = []
for _ in range(R):
    rows = list(input().rstrip())
    maps.append(rows)

J_starts = []
F_starts = []

for row in range(R):
    for col in range(C):
        if maps[row][col] == 'F':
            F_starts.append((row, col, 'F'))
        elif maps[row][col] == 'J':
            J_starts.append((row, col, 'J'))

starts = F_starts + J_starts

q = deque(starts)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = 1
escape = False
while q:
    for _ in range(len(q)):
        row, col, now_type = q.popleft()
        if now_type == 'J':
            if row == 0 or col == 0 or row == (R - 1) or col == (C - 1):
                escape = True
                break
        for i in range(4):
            r, c = dr[i], dc[i]
            if 0 <= (row + r) and (row + r) < R and 0 <= (col + c) and (col + c) < C:
                if maps[row + r][col + c] != '#':
                    if now_type == 'J':
                        if maps[row + r][col + c] == '.':
                            maps[row + r][col + c] = 'J'
                            q.append((row + r, col + c, now_type))
                        if maps[row + r][col + c] == 'F':
                            if maps[row][col] == 'J' or maps[row][col] == '.': # 불을 만나서 뒷걸음질
                                q.append((row, col, now_type))
                    else:
                        if maps[row + r][col + c] != 'F':
                            maps[row + r][col + c] = 'F'
                            q.append((row + r, col + c, now_type))
    
    if escape: break
    answer += 1

if escape:
    print(answer)
else:
    print('IMPOSSIBLE')
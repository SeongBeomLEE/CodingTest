# 큐2
from collections import deque
from sys import stdin
que = deque([])
for _ in range(int(stdin.readline())):
    line = stdin.readline().split()
    if line[0] == 'push': que.append(line[1])
    if line[0] == 'pop':
        if que: print(que.popleft())
        else: print(-1)
    if line[0] == 'size': print(len(que))
    if line[0] == 'empty':
        if que : print(0)
        else: print(1)
    if line[0] == 'front':
        if que: print(que[0])
        else: print(-1)
    if line[0] == 'back':
        if que: print(que[-1])
        else: print(-1)
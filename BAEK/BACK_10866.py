# 덱
from collections import deque
from sys import stdin
_degue = deque([])
for _ in range(int(stdin.readline())):
    line = stdin.readline().split()
    if line[0] == 'push_front':
        _degue.appendleft(line[1])
    if line[0] == 'push_back':
        _degue.append(line[1])
    if line[0] == 'pop_front':
        if _degue: print(_degue.popleft())
        else: print(-1)
    if line[0] == 'pop_back':
        if _degue: print(_degue.pop())
        else: print(-1)
    if line[0] == 'size': print(len(_degue))
    if line[0] == 'empty':
        if _degue: print(0)
        else: print(1)
    if line[0] == 'front':
        if _degue: print(_degue[0])
        else: print(-1)
    if line[0] == 'back':
        if _degue: print(_degue[-1])
        else: print(-1)
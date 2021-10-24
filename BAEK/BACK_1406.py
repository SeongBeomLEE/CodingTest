# 에디터
from sys import stdin
from collections import deque

stack_l = list(stdin.readline().strip())
stack_r = deque()
n = int(input())
for m in stdin:
    if m[0] == 'L':
        if stack_l: stack_r.appendleft(stack_l.pop())
        else: continue
    if m[0] == 'D':
        if stack_r: stack_l.append(stack_r.popleft())
        else: continue
    if m[0] == 'B':
        if stack_l: stack_l.pop()
        else: continue
    if m[0] == 'P':
        stack_l.append(m[2])

print(''.join(stack_l + list(stack_r)))

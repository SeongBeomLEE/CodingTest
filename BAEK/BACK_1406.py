# 에디터
from sys import stdin

stack_l = list(stdin.readline().strip())
stack_r = []
n = int(input())
for m in stdin:
    if m[0] == 'L':
        if stack_l: stack_r.append(stack_l.pop())
        else: continue
    if m[0] == 'D':
        if stack_r: stack_l.append(stack_r.pop())
        else: continue
    if m[0] == 'B':
        if stack_l: stack_l.pop()
        else: continue
    if m[0] == 'P':
        stack_l.append(m[2])

print(''.join(stack_l + list(reversed(stack_r))))

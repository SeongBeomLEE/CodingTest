# https://www.acmicpc.net/problem/9012
# 괄호
import sys
input = sys.stdin.readline
answer = 0
for _ in range(int(input())):
    command = input().rstrip()
    left_stack = []
    for c in command:
        if c == '(':
            left_stack.append(c)
        else:
            if left_stack: left_stack.pop()
            else:
                left_stack.append(c) 
                break
    if left_stack: print('NO')
    else: print('YES')
# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상
import sys
input = sys.stdin.readline

while True:
    command = input().rstrip()
    if command == '.': break
    left_stack = []
    for c in command:
        if c == '(' or c == '[':
            left_stack.append(c)
        elif c == ')':
            if left_stack:
                if left_stack[-1] == '(': 
                    left_stack.pop()
                else:
                    left_stack.append(c) 
                    break
            else:
                left_stack.append(c)  
                break
        elif c == ']':
            if left_stack:
                if left_stack[-1] == '[': 
                    left_stack.pop()
                else:
                    left_stack.append(c)  
                    break
            else:
                left_stack.append(c)  
                break
        elif c == '.': break
    
    if left_stack: print('no')
    else: print('yes')
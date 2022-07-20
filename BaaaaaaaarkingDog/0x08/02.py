# https://www.acmicpc.net/problem/3986
# 좋은 단어
import sys
input = sys.stdin.readline
answer = 0
for _ in range(int(input())):
    command = input().rstrip()
    left_stack = []
    for c in command:
        if left_stack:
            if left_stack[-1] == c: left_stack.pop()
            else: left_stack.append(c)
        else: 
            left_stack.append(c)
    
    if not left_stack:
        answer += 1

print(answer)
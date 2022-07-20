# https://www.acmicpc.net/problem/10799
# 쇠막대기
import sys
input = sys.stdin.readline
answer = 0
command = input().rstrip()
stack = []

for idx, c in enumerate(command):
    if c == '(':
        stack.append(c)
    else:
        if command[idx - 1] == '(': # 레이저 발사
            stack.pop()
            answer += len(stack)
        else: # 막대기 종료
            stack.pop()
            answer += 1
print(answer)
# 옥상 정원 꾸미기
import sys
n = int(sys.stdin.readline())
b_li = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
ret = 0
for idx in range(n):
    while stack and stack[-1] <= b_li[idx]:
        stack.pop()
    stack.append(b_li[idx])
    ret += len(stack) - 1

print(ret)

# 오큰수
from sys import stdin

N = int(input())
A = list(map(int, stdin.readline().strip().split()))
answer = [-1 for _ in range(N)]
stack = [0]
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

for i in answer:
    print(i, end=' ')
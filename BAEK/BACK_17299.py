# 오등큰수
from sys import stdin
from collections import Counter

N = int(input())
A = list(map(int, stdin.readline().strip().split()))
A_dic = Counter(A)

stack = [0]
answer = [-1 for _ in range(N)]

for idx in range(1, N):
    while stack and A_dic[A[stack[-1]]] < A_dic[A[idx]]:
        answer[stack.pop()] = A[idx]
    stack.append(idx)

for i in answer:
    print(i, end = ' ')
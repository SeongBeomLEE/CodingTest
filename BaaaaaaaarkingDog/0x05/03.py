# https://www.acmicpc.net/problem/1874
# 스택 수열

import sys
input = sys.stdin.readline
N = int(input())
answer = []
left_array = []
rihgt_array = [i for i in range(1, N + 1)][::-1]

for _ in range(N):
    command = int(input())
    if not left_array:
        answer.append('+')
        left_array.append(rihgt_array.pop())
    while left_array[-1] != command:
        if not rihgt_array: break
        answer.append('+')
        left_array.append(rihgt_array.pop())
    else:
        answer.append('-')
        left_array.pop()

if left_array:
    print('NO')
else:
    for i in answer:
        print(i)

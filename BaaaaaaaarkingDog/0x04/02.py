# https://www.acmicpc.net/problem/5397
# 키로거
# 스택을 사용한 풀이 (연결리스트로 못 풀겠어요.....)

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    
    command = input().rstrip()

    left, right = [], []

    for c in command:
        if c == ">":
            if right:
                left.append(right.pop())
        elif c == '<':
            if left:
                right.append(left.pop())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)

    print("".join(left) + "".join(right[::-1]))
# https://www.acmicpc.net/problem/5430
# AC
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ps = input().rstrip()
    n = int(input())
    array = deque(input().rstrip()[1:-1].split(","))
    if n == 0: array = deque([])
    rev = 0
    for p in ps:
        if p == 'R':
            rev += 1
        elif p == 'D':
            if array:
                if rev % 2 == 0:
                    array.popleft()
                else:
                    array.pop()
            else:
                print('error')
                break
    else:
        if rev % 2 == 0:
            print('[' + ','.join(list(array)) + ']')
        else:
            print('[' + ','.join(list(array)[::-1]) + ']')
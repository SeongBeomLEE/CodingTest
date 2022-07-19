# https://www.acmicpc.net/problem/2164
# 카드2
import sys
from collections import deque
input = sys.stdin.readline

array = deque([i + 1 for i in range(int(input()))])

action = True # True 면 버리기, False면 제일 위로 옮기기

while len(array) != 1:
    if action:
        array.popleft()
        action = False
    else:
        array.append(array.popleft())
        action = True

print(array[0])
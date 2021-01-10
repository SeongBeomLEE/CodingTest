import sys

result = [0]*10001

for _ in range(int(input())):
    N = int(sys.stdin.readline())
    result[N] += 1

for i in range(10001):
    if result[i] != 0:
        for _ in range(result[i]): print(i)
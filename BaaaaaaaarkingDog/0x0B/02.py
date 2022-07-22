# https://www.acmicpc.net/problem/11729
# 하노이 탑 이동 순서
import sys
input = sys.stdin.readline
K = int(input())

print(2**K - 1)

def solution(a, b, n):
    if n == 1:
        print(a, b)
        return
    solution(a, 6-a-b, n-1)
    print(a, b)
    solution(6-a-b, b, n-1)

solution(1, 3, K)


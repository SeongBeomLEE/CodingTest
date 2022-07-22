# https://www.acmicpc.net/problem/1629
# 곱셈
import sys
input = sys.stdin.readline
A, B, C = map(int, input().rstrip().split(" "))

def POW(a, b, c):
    if b == 1: return a % c
    val = POW(a, b // 2, c)
    val = val**2 % c
    if b % 2 == 0: return val
    return val * a % c

print(POW(A, B, C))
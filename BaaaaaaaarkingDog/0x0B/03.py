# https://www.acmicpc.net/problem/1074
# Z
import sys
input = sys.stdin.readline
N, r, c = map(int, input().rstrip().split(" "))

def solution(n, r, c):
    if n == 0: return 0
    half = 2 ** (n - 1)
    if r < half and c < half: return solution(n - 1, r, c) # 1사분면
    if r < half and half <= c: return half * half + solution(n - 1, r, c - half) # 2사분면 : c 에 변화를 줘서 1사분면으로 바꾸기
    if half <= r and c < half: return 2 * half * half + solution(n - 1, r - half, c) # 3사분면 : r 에 변화를 줘서 1사분면으로 바꾸기
    if half <= r and half <= c: return 3 * half * half + solution(n - 1, r - half, c - half) # 4사분면 : r과 c 에 변화를 줘서 1사분면으로 바꾸기

print(solution(N, r, c))
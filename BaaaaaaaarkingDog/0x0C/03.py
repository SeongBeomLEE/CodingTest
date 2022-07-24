# https://www.acmicpc.net/problem/1182
# 부분수열의 합
import sys
input = sys.stdin.readline
N, S = map(int, input().rstrip().split(' '))
values = list(map(int, input().rstrip().split(' ')))
answer = 0

def solution(value, start_idx):
    global answer
    if value == S: answer += 1
    for idx in range(start_idx + 1, N):
        solution(value + values[idx], idx)

for idx in range(N):
    solution(values[idx], idx)

print(answer)
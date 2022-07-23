# https://www.acmicpc.net/problem/2630
# 쿼드트리
import sys
input = sys.stdin.readline
N = int(input())
video = []
for _ in range(N):
    video.append(list(input().rstrip()))

def solution(x, y, N):
    check = video[x][y]
    for dx in range(N):
        for dy in range(N):
            if check != video[x + dx][y + dy]:
                answer = '('
                for i in range(2):
                    for j in range(2):
                        answer += solution(x + i * N // 2, y + j * N // 2, N // 2)
                return answer + ')'

    if check == '0': return '0'
    if check == '1': return '1'

print(solution(0, 0, N))
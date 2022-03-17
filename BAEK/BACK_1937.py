# 욕심쟁이 판다
import sys
sys.setrecursionlimit(10**6)

N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dp = [[0] * N for _ in range(N)]

def get_answer(r = 0, c = 0):
    if dp[r][c] != 0: return dp[r][c]
    if dp[r][c] == 0:
        dp[r][c] = 1
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < N:
                if maps[r][c] < maps[nr][nc]:
                    dp[r][c] = max(dp[r][c], get_answer(nr, nc) + 1)
    return dp[r][c]

answer = 0
for r in range(N):
    for c in range(N):
        answer = max(answer, get_answer(r = r, c = c))

print(answer)
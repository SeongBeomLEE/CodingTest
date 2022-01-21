# 녹색 옷 입은 애가 젤다지?
from collections import deque
cnt = 1
while True:
    n = int(input())
    if n == 0 : break

    maps = []
    for _ in range(n):
        maps.append(list(map(int, input().split())))

    # 정보를 저장시킬 테이블을 만드는 것이 다익스트라 알고리즘의 핵심
    INF = 987654321
    dp = [[INF for _ in range(n)] for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque([[0, 0]])
    dp[0][0] = maps[0][0]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if dp[x][y] + maps[nx][ny] < dp[nx][ny]:
                    dp[nx][ny] = dp[x][y] + maps[nx][ny]
                    q.append([nx, ny])

    print(f'Problem {cnt}: {dp[n-1][n-1]}')
    cnt += 1
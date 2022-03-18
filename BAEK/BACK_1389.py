# 케빈 베이컨의 6단계 법칙
# 최단 거리 알고리즘 활용
def dijkstra(i, cnt):
    for j in array[i]:
        if cnt + 1 < dp[j]:
            dp[j] = cnt + 1
            dijkstra(j, cnt + 1)

N, M = map(int, input().split())
array = [[] for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    array[i - 1].append(j - 1)
    array[j - 1].append(i - 1)

INF = 987654321
answer = []
for i in range(N):
    dp = [INF] * N
    dp[i] = 0
    dijkstra(i, 0)
    answer.append(sum(dp))

print(answer.index(min(answer)) + 1)
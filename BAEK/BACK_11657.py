# 타임머신
'''
다익스트라 알고리즘과 다른 점은
V - 1개의 반복 + e의 반복을 통해서
새롭게 또 값이 갱신되면 음의 사이클이 발생했다고 판단하는 것
따라서 시간 복잡도는 O(VE)가 됨
'''

N, M = map(int, input().split())
maps = []

for _ in range(M):
    maps.append(list(map(int, input().split())))

INF = 987654321
dp = [INF] * N
dp[0] = 0
neg_cycle = False

for n in range(N):
    for i, j, c in maps:
        if dp[i - 1] + c < dp[j - 1] and dp[i - 1] != INF:
            dp[j - 1] = dp[i - 1] + c
            if n == N - 1:
                neg_cycle = True

if neg_cycle: print(-1)
else:
    for i in dp[1:]:
        if i == INF: print(-1)
        else: print(i)
'''
다익스트라 알고리즘을 활용한 풀이
'''
from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n)]
    for a, b in edge:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    dp = [987654321] * n
    start_node = 0
    cnt = 0
    q = deque([[start_node, cnt]])
    while q:
        a, cnt = q.popleft()
        cnt += 1
        for b in graph[a]:
            if cnt < dp[b]:
                dp[b] = cnt
                q.append([b, cnt])
    dp[0] = 0
    answer = dp.count(max(dp))
    return answer
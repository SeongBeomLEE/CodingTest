# 합승 택시 요금
# 다익스트라 알고리즘의 활용 문제
import heapq
def dijkstra(n, s, graph):
    INF = 987654321
    dist = [INF] * (n + 1)
    dist[s] = 0
    q = []
    heapq.heappush(q, [0, s])
    while q:
        now_cost, now_node = heapq.heappop(q)

        # 이 부분이 시간복자도를 줄여줌
        if dist[now_node] < now_cost:
            continue

        for next_node, cost in graph[now_node]:
            next_cost = now_cost + cost
            if dist[next_node] > next_cost:
                dist[next_node] = next_cost
                heapq.heappush(q, [next_cost, next_node])

    return dist

def solution(n, s, a, b, fares):
    answer = 987654321
    graph = [[] for _ in range(n + 1)]
    for v1, v2, cost in fares:
        graph[v1].append([v2, cost])
        graph[v2].append([v1, cost])

    s_dist = dijkstra(n = n, s = s, graph = graph)
    for i in range(1, n + 1):
        dist = dijkstra(n = n, s = i, graph = graph)
        answer = min(answer, dist[a] + dist[b] + s_dist[i])

    return answer
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))
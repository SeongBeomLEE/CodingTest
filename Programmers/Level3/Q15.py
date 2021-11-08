# 가장 먼 노드
from collections import deque
def solution(n, edge):
    v = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        a, b = e
        graph[a] += [b]
        graph[b] += [a]
    q = deque(graph[1])
    dis = 1
    while q:
        # 현재 방문해야할 노드의 개수 만큼 반복됨
        for _ in range(len(q)):
            b = q.popleft()
            if v[b] == 0:
                v[b] = dis
                for b in graph[b]: q.append(b)
        dis += 1
    del v[1]
    return v.count(max(v))

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))

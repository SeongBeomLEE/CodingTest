# 순위
from collections import deque
def solution(n, results):
    fight = [[0] * n for _ in range(n)]
    graph = [[] for _ in range(n)]
    answer = n

    for result in results:
        w, l = result
        fight[w - 1][l - 1] = 1
        fight[l - 1][w - 1] = -1
        graph[w - 1].append(l - 1)

    for w, result in enumerate(graph):
        q = deque(graph[w])
        vis = [w]
        while q:
            l_li = []
            for _ in range(len(q)):
                l = q.popleft()
                vis += [l]
                fight[w][l] = 1
                fight[l][w] = -1
                l_li.append(l)
            # 쓸데없는 방문을 제거하기 위해서
            for l in l_li:
                for i in graph[l]:
                    if i not in vis:
                        q.append(i)

    for result in fight:
        cnt = 0
        for r in result:
            if r == 0 : cnt += 1
            if cnt > 1:
                answer -= 1
                break

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))

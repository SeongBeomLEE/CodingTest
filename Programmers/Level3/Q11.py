# 네트워크
def solution(n, computers):
    answer = 1
    graph = [[] for _ in range(n)]
    for a, computer in enumerate(computers):
        for b, c in enumerate(computer):
            if c == 1:
                graph[a] += [b]
    visit = [0] * n
    q = [0]
    while q or 0 in visit:
        if not q:
            answer += 1
            q.append(visit.index(0))
        a = q.pop(0)
        visit[a] = 1
        for b in graph[a]:
            if visit[b] == 0: q.append(b)
    return answer
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
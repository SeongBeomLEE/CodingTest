# 배달
def solution(N, road, K):
    INF = 987654321
    answer = [INF for _ in range(N + 1)]
    path = [[] for _ in range(N + 1)]
    for s, e, c in road:
        path[s].append((e, c))
        path[e].append((s, c))

    stack = [[1, 0, []]]
    while stack:
        s, c, vis = stack.pop()
        if c <= K:
            _vis = list(vis) + [s]
            answer[s] = min(answer[s] , c)
            for p in path[s]:
                _e, _c = p
                if _e not in _vis:
                    if c + _c < answer[_e]:
                        stack.append([_e, c + _c, _vis])
    cnt = 0
    for k in answer:
        if k <= K: cnt += 1

    return cnt

N = 6
road = [[1,2,7],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4
print(solution(N, road, K))
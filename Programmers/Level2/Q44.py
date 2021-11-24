# 전력망을 둘로 나누기
from collections import deque
def solution(n, wires):
    answer = 100
    map = [[] for _ in range(n)]
    for wire in wires:
        v1, v2 = wire
        map[v1 - 1].append(v2 - 1)
        map[v2 - 1].append(v1 - 1)

    for wire in wires:
        v1, v2 = wire
        map[v1 - 1].remove(v2 - 1)
        map[v2 - 1].remove(v1 - 1)
        for s in range(n):
            vis = [0] * n
            q = deque([s])
            cnt1 = 0
            while q:
                start = q.popleft()
                vis[start - 1] = 1
                cnt1 += 1
                for next in map[start]:
                    if vis[next - 1] == 0:
                        q.append(next)
            answer = min(answer, abs(n - (cnt1 * 2)))

        map[v1 - 1].append(v2 - 1)
        map[v2 - 1].append(v1 - 1)

    return answer

n = 8
wires = [[1, 2], [2, 3], [2, 4], [2, 5], [5, 8], [5, 7], [5, 6]]
print(solution(n, wires))
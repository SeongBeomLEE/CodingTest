# 섬 연결하기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    parent = [0] * (n)
    edges = []
    answer = 0

    for i in range(0, n):
        parent[i] = i

    for a, b, c in costs:
        edges.append((c, a, b))

    edges.sort()
    for edge in edges:
        c, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += c

    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))
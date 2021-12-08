# 네트워크
# 서로소 집합 활용
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def solution(n, computers):
    parent = [i for i in range(n)]

    # 노드 속 부모 노드 찾기
    for i in range(n):
        a = find_parent(parent, i)
        for j in range(n):
            if i != j and computers[i][j] == 1:
                b = find_parent(parent, j)
                if a <= b: parent[b] = a
                else: parent[a] = b

    # 전체 그래프의 노드 연결
    for i in range(n):
        parent[i] = find_parent(parent, i)
    return len(set(parent))
n = 5
computers = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1]]
print(solution(n, computers))
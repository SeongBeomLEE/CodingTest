# 서로소 집합을 활용한 크루스칼 알고리즘 (합승 택시 요금 문제 활용함)
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

def solution(n, fares):
    answer = 0
    # 크루스칼 알고리즘의 경우 무조건 비용 순으로 정렬을 해야 최적 해를 보장함
    fares = sorted(fares, key = lambda x: x[2])
    parent = [i for i in range(n + 1)]

    for a, b, cost in fares:
        print(a, b, parent)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer

n = 6
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, fares))
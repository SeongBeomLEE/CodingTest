# 달팽이가 하루에 올가가는 길이 A-B
# (V-B) // (A-B)는 달팽이가 올라가야할 총 일수
# 그런데 (V-B) % (A-B) 가 0이 아니라면 하루를 더 올라갸아 함

def solution(A, B, V):
    ret = ((V-B) // (A-B))
    if ((V-B) % (A-B)) != 0: return ret + 1
    return ret

A, B, C = map(int,input().split())

print(solution(A, B, C))
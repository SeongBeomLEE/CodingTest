# 최솟값 만들기
def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    answer = 0
    for a, b in zip(A, B):
        answer += a * b
    return answer
A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A,B))
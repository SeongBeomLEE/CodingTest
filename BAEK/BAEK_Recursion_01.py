# 밑 함수를 풀어쓰면
# 5 * solution(4)
# solution(4) = 4 * solution(3)
# solution(3) = 3 * solution(2)
# solution(2) = 2 * solution(1)
# solution(1) = 1
# 합치면
# return 5 * 4 * 3 * 2 * 1
def solution(n):
    if n <= 1 : return 1
    else: return n * solution(n-1)

N = int(input())
print(solution(N))
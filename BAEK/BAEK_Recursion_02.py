# 밑 함수를 풀어쓰면
# s(5) = s(4) + s(3)
# s(4) = s(3) + s(2)
# s(3) = s(2) + s(1)
# s(2) = s(1) + s(0)
# s(1) = 1
# s(0) = 0

# s(5) = s(4) / s(3)
#      = s(3) + s(2) / s(3)
#      = s(2) + s(1) + s(2) / s(2) + s(1)
#      = s(1) + s(0) + s(1) + s(1) + s(0) / s(1) + s(0) + s(1)
#      =   1  +  0   +   1  +   1  +   0  +   1 +    0  +  1
#      = 5
def solution(N):
    if N <= 1:
        return N
    return solution(N-1) + solution(N-2)

N = int(input())
print(solution(N))
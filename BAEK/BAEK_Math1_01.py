# A: 고정비, B: 가변비, C: 가격, n는 판매대수
# 손익 분기점: A+nB < nC
# A/nC + B/C > 1
# n 이 무한대로 간다면 의미가 없어 A/nC는 의미가 없어지므로 B/C >= 0 면 손익분기점이 존재하지 않음
# n을 구하기 위해서는 n을 하나의 식으로 만들어야 해
# A < (C-B)n
# A / (C-B) < n
def solution(A, B, C):
    ret = -1
    if ((B/C) >= 1): return ret
    else:
        ret = int( (A/(C-B)) ) + 1
        return ret

A, B, C = map(int,input().split())
print(solution(A, B, C))
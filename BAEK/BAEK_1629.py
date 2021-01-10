def solution(A,B,C):
    ret = 1
    while B:
        # 이진수를 활용한 풀이법
        # ex) A^11
        # 11은 2진수로 1011
        # A^11=A^1 * A^2 * A^0 * A^8
        if B % 2 == 1 : ret = ret * A % C
        A = A * A % C
        B //=2
    return ret
A,B,C = map(int,input().split(" "))
print(solution(A,B,C))
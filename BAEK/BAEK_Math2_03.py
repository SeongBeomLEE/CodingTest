# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수
# 에라토스테네스의 체
# ck는 전체 소수의 배열
# False는 소수인 숫자의 자리, True는 소수가 아닌 숫자의 자리
# p는 소수가 저장될 리스트
# 아이디어
# 반대로 생각한 거임
# ex) 2가 소수면 일단은 2의 배수들은 다 True 즉 다 소수가 아님
# 이렇게 작은 수 마다 넣으면서 True인 자리의 작은 수가 나오면 그 반복을 건너뜀
# 이런식으로 2부터 판별할 숫자까지 리스트를 만듬
def era(M, N):
    ck, p =[False for _ in range(N+1)], []
    for i in range(2, N+1):
        if ck[i] == True : continue
        if i >= M:
            p.append(i)
        for j in range(i*i, N+1, i):
            ck[j] = True
    return p

M, N = map(int, input().split())
prime = era(M,N)
for i in prime: print(i)
# 최대공약수 구하기
# 유클리드 호제법
def gcd(a, b):
    return b if a%b==0 else gcd(b, a%b)

# 최소공배수
def lcm(a, b):
    return a*b/gcd(a, b)

# 소수 찾기
# 에라토스테네스의 체
def era(N):
    # ck는 전체 소수의 배열
    # False는 소수인 숫자의 자리, True는 소수가 아닌 숫자의 자리
    # p는 소수가 저장될 리스트
    ck, p =[False for _ in range(N+1)], []
    for i in range(2, N+1):
        if ck[i] == True : continue
        p.append(i)
        for j in range(i*i, N+1, i):
            ck[j] = True
    return ck, p
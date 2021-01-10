# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수
def isPrime(x):
    if x == 1 : return False
    for i in range(2, int(x/2)+1):
        if(x%i == 0): return False
    return True # 소수

_ = int(input())
prime = list(map(int,input().split()))
count = 0
for i in prime:
    if isPrime(i):
        count +=1

print(count)
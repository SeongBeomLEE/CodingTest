'''
직전에는 무조건 1이 되어야 함
c = b - a (이동해야할 총 거리)
1 1 1     num**2  num = 1
2 2 1+1
3 3 1+1+1

4((num)**2)       3(num*2 -1) 1+2+1  (num + 1)**2
5                 4(num*2)    1+2+1+1
6((num)**2 + num) 4(num*2)    1+2+2+1
7                 5(num*2 +1) 1+2+2+1+1
8                 5(num*2 +1) 1+2+2+2+1

9 5 1+2+3+2+1 (num+2)**2
10 6 1+2+3+2+1+1
'''
def solution():
    a, b = map(int,input().split())
    c = b-a

    num = 1
    while True:
        if num**2 <= c < (num+1)**2: break
        num += 1

    if c == (num**2): return num*2 -1
    elif (num**2) < c <=(num**2 + num): return num*2
    else: return num*2 + 1

t = int(input())
for i in range(t):
    print(solution())
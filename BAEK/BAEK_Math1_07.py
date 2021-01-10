# 3층 1 5 15 35 70
# 2층 1 4 10 20 35
# 1층 1 3 6 10 15
# 0층 1 2 3 4 5
# k층에 n호에 사는 사람
# 아이디어
# 1. 밑바닥 층 부터 구한다.
# f = [i for i in range(1, n+1)]
# 2. 층이 하나씩 올라간다.
# for _ range(k):
# 3. 층이 올라갈때 마다 하나씩 더해간다
# for i in range(1, num): 인덱스는 0부터 시작하니깐 num까지만 반복 또한 인덱스 0은 계속 1임
# f[i] = f[i] + f[i-1]
# 4. 마지막 수를 출력한다
# f[-1]

def solution(k, n):
    f = [i for i in range(1,n+1)]
    for _ in range(k):
        for i in range(1, n):
            f[i] = f[i] + f[i-1]

    return f[-1]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(solution(k,n))
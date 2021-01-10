# H 호텔의 층수
# W 각 층의 방수
# N 몇번째 손님
# 방번호 XXYY
# 아이디어
# 1. N % H의 나머지를 판별한다
# 2. N % H의 나머지가 0이면 H는 XX,  N//H가 YY
# 3. N % H의 나머지가 0이 아니면 N % H이 XX, N // H + 1가 YY
def solution(H, W, N):
    X = N % H
    Y = N // H + 1
    if X == 0: return H, Y-1
    return X, Y

T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())
    X, Y = solution(H, W, N)
    print(X * 100 + Y)
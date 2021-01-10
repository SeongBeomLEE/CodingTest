# 아이디어
# N/2인 수 중 부터 시작하여 왼쪽 오른쪽으로 이동하여 골드바흐에 조건에 맞는 값을 찾아가자
def era(N):
    prime_array, prime_number = [False for _ in range(N+1)], []
    for i in range(2, N+1):
        if prime_array[i] == True: continue
        prime_number.append(i)
        for j in range(i*i, N+1, i):
            prime_array[j] = True
    return prime_number

def gold(N):
    prime_list = era(N)
    idx = max([i for i in range(len(prime_list)) if prime_list[i] <= N/2])
    for i in range(idx, -1, -1): # i는 n/2부터 왼쪽으로 이동
        for j in range(i, len(prime_list)): # j는 n/2부터 오른쪽으로 이동
            if prime_list[i] + prime_list[j] == N:
                return [prime_list[i], prime_list[j]]

for _ in range(int(input())):
    print(" ".join(map(str,gold(int(input())))))

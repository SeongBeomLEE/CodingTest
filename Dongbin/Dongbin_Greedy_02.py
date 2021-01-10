# 큰 수의 법칙
# 우리에게 필요한 수는
# 제일 큰 수와 두번째로 큰수
# M을 하나씩 빼서 0이되면 반복을 멈추자

# N이 배열의 크기, M이 숫자가 더해지는 횟수, K번 더한다.

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
# 정렬
# 1, 2, 3
numbers.sort(reverse=True)
# 3, 2, 1
first = numbers[0]
secnde = numbers[1]
result = 0

while True:
    for _ in range(K):
        if M == 0: break
        result += first
        M -= 1
    if M == 0 : break
    result += secnde
    M -= 1

print(result)




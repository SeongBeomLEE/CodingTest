def solution(n):
    answer = 0
    coin_type = [500, 100, 50, 10]
    for coin in coin_type:
        answer += n // coin
        n = n % coin

    return answer

n = 1260
print(solution(n))

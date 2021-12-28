def solution(n, k):
    answer = 0
    while True:
        target = (n // k) * k
        answer += n - target
        n = target
        if n < k:
            break
        answer += 1
        n //= k

    answer += (n - 1)

    return answer

n, k = 25, 5
print(solution(n, k))
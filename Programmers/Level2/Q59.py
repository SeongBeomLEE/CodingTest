# 숫자의 표현
def solution(n):
    answer = 1
    end = int(n / 2) + 1
    for i in range(1, end + 1):
        cnt = 0
        for j in range(i, end + 1):
            cnt += j
            if cnt >= n:
                if cnt == n: answer += 1
                break
    return answer
n = 15
print(solution(n))
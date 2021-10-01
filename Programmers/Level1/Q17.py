# 3진법 뒤집기
def solution(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n, 3)
        answer += str(mod)
    return int(answer, 3)
n = 45
print(solution(n))
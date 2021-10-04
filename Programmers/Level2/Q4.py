#124 나라의 숫자
def solution(n):
    answer = ''

    while n > 0:
        # 몫, 나머지
        n, mod = divmod(n, 3)
        if mod == 0:
            mod = (n * 3) - ((n - 1) * 3)
            n -= 1
        if mod == 3:
            mod = 4

        answer += str(mod)

    return answer[::-1]

print(solution(3, 3))
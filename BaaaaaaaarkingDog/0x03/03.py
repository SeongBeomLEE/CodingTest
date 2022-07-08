# https://www.acmicpc.net/problem/1475
# 방 번호

def solution(num : str):
    answer = [0] * 10
    for n in num:
        if n == '6':
            if answer[int(n)] <= answer[int("9")]: answer[int(n)] += 1
            else: answer[int("9")] += 1
        elif n == '9':
            if answer[int(n)] <= answer[int("6")]: answer[int(n)] += 1
            else: answer[int("6")] += 1
        else: answer[int(n)] += 1
    return max(answer)

num = input()
print(solution(num))
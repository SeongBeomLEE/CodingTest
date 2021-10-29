# N으로 표현
def solution(N, number):
    answer = [[]] + [[int(str(N) * i)] for i in range(1, 9)]
    # ex) i = 2 / 3
    for i in range(1, 9):
        # j = 1 / 1
        for j in range(1, i):
            # 1개를 사용한 값들 / 1개를 사용한 값들
            for a in answer[j]:
                # 1개를 사용한 값들 / 2개를 사용한 값들
                for b in answer[i - j]:
                    answer[i].append(a + b)
                    answer[i].append(a * b)
                    answer[i].append(a - b)
                    if b != 0 : answer[i].append(a // b)
        if number in answer[i]: return i
    return -1

N = 4
number = 17
print(solution(N, number))
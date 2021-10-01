# 2016년
def solution(a, b):
    for i in range(1, a):
        if i <= 7:
            if i == 2: b += 29
            elif i % 2 == 0: b += 30
            else: b += 31
        else:
            if i % 2 == 0: b += 31
            else: b += 30
    b = b % 7
    answer = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    return answer[b]
a = 11
b = 30
print(solution(a, b))
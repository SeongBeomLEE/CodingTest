# 비밀지도
def get_2(num, n):
    s = ''
    while num != 0:
        num, _s = divmod(num, 2)
        s += str(_s)
    s = s[::-1]
    s = '0' * (n - len(s)) + s
    return s

def solution(n, arr1, arr2):
    arr1 = [get_2(num, n) for num in arr1]
    arr2 = [get_2(num, n) for num in arr2]
    answer = []
    for ar1, ar2 in zip(arr1, arr2):
        s = ''
        for a1, a2 in zip(ar1, ar2):
            if a1 == '0' and a2 == '0':
                s += ' '
            else: s += '#'
        answer.append(s)
    return answer
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
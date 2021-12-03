# 다음 큰 숫자
def solution(n):
    cnt = str(bin(n)).count('1')
    for _n in range(n + 1, 1000001):
        _cnt = str(bin(_n)).count('1')
        if cnt == _cnt:
            answer = _n
            break
    return answer

n = 78
print(solution(n))
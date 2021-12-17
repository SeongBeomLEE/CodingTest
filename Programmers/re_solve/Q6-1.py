'''
1. 잊어버린 학생들 중에서 여벌의 체육복이 존재하는 친구들을 먼저 제거한다.
2. 잊어버린 학생 + 1 의 친구들을 제거한다.
3. 잊어버린 학생 - 1 의 친구들을 제거한다.
4. 전체 학생 수 - 잊어버린 학생 수 반환

12345678

1 2 3 4 5 6 7

1 3 5 7 9
'''


def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in range(1, n + 1):
        if i in lost:
            if i in reserve:
                lost.remove(i)
                reserve.remove(i)

    for r in reserve:
        b = r + 1
        f = r - 1
        if f in lost:
            lost.remove(f)
        elif b in lost:
            lost.remove(b)

    answer = n - len(lost)
    return answer
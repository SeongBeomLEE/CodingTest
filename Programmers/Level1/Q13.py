# 체육복
def solution(n, lost, reserve):
    reserve.sort()
    lost.sort()
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


def solution(n, lost, reserve):
    answer = []
    lost.sort()
    reserve.sort()
    for i in lost:
        if i not in reserve:
            if i - 1 in reserve:
                if i - 1 not in lost:
                    reserve.remove(i - 1)
                    answer.append(i)
            elif i + 1 in reserve:
                if i + 1 not in lost:
                    reserve.remove(i + 1)
                    answer.append(i)
        else:
            reserve.remove(i)
            answer.append(i)
    answer = n - (len(lost) - len(answer))
    return answer

# 전체 학생의 수
n = 5
# 도난당한 학생들의 번호가 담긴 배열
lost = [2, 4]
# 여별의 체육복을 가져온 학생들의 번호가 담긴 배열
reserve = [1, 3, 5]
print(solution(n, lost, reserve))
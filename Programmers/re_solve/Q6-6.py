'''
[[-20,15], [-14,-5], [-18,-13], [-5,-3]]

1. right 값을 기준으로 나열한다.
2. 가장 작은 right 값을 가진 친구로 시작한다.
3. 다음 값의 기준은 위에서 구한 right 값보다 큰 left 값을 가진 친구의 right 값
4. 3번 과정을 끝날때까지 반복한다.

'''


def solution(routes):
    routes.sort(key=lambda x: x[1])
    standard = 0
    answer = 1
    for idx in range(len(routes)):
        if routes[idx][0] <= routes[standard][1]:
            continue
        else:
            answer += 1
            standard = idx
    return answer
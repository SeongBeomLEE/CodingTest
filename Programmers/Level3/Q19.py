# 셔틀버스
# n - 셔틀 운행 횟수
# t - 셔틀 운행 간격
# m - 한 셔틀에 탈 수 있는 최대 크루 수
# timetable - 크루가 대기열에 도착하는 시각을 모은 배열
from collections import deque

def get_time(x):
    h, m = x.split(':')
    time = (int(h) * 60) + int(m)
    return time

def solution(n, t, m, timetable):
    timetable = deque(sorted(list(map(lambda x: get_time(x), timetable))))
    start = get_time('09:00')
    total_m = 0
    for _ in range(n):
        _m = 0
        while True:
            if abs(_m) == m:
                answer = ans - 1
                break
            if not timetable:
                answer = start
                break
            if timetable[0] <= start:
                ans = timetable.popleft()
                _m -= 1
            else:
                answer = start
                break
        total_m += abs(_m)
        start += t
        if total_m >= (n * m): break

    h = str(answer // 60)
    m = str(answer % 60)
    if len(h) == 1: h = '0' + h
    if len(m) == 1: m = '0' + m
    answer = f'{h}:{m}'
    return answer
n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
print(solution(n, t, m, timetable))
# 추석 트래픽
def get_time(x):
    year, time, end = x.split(' ')
    end = float(end[:-1])
    h, m, s = time.split(':')
    end_time = (float(h) * 3600) + (float(m) * 60) + float(s)
    start_time = round(end_time - end + 0.001, 3)
    return start_time, end_time

def solution(lines):
    answer = 0
    for idx, line in enumerate(lines):
        start_time, end_time = get_time(line)
        start_cnt = 1
        end_cnt = 1
        for _line in lines[idx + 1:]:
            _start_time, _end_time = get_time(_line)

            if _start_time <= round(start_time + 0.999, 3) and start_time <= _end_time:
                start_cnt += 1

            if end_time <= _end_time and _start_time <= round(end_time + 0.999, 3):
                end_cnt += 1

        answer = max(answer, max(start_cnt, end_cnt))

    return answer

lines =  [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

print(solution(lines))
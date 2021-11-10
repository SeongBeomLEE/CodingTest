# 광고 삽입
# https://dev-note-97.tistory.com/156
def solution(play_time, adv_time, logs):
    h, m, s = map(int, play_time.split(':'))
    play_time = (h * 3600) + (m * 60) + s

    h, m, s = map(int, adv_time.split(':'))
    adv_time = (h * 3600) + (m * 60) + s

    all_time = [0] * (play_time + 1)

    for log in logs:
        start, end = log.split('-')
        s_h, s_m, s_s = map(int, start.split(':'))
        e_h, e_m, e_s = map(int, end.split(':'))

        s_t = (s_h * 3600) + (s_m * 60) + s_s
        e_t = (e_h * 3600) + (e_m * 60) + e_s

        all_time[s_t] += 1
        all_time[e_t] -= 1

    for i in range(1, play_time + 1):
        all_time[i] += all_time[i - 1]

    for i in range(1, play_time + 1):
        all_time[i] += all_time[i - 1]

    max_view = 0
    max_time = 0
    for i in range(adv_time -1, play_time):
        if (i >= adv_time):
            if max_view < all_time[i] - all_time[i - adv_time]:
                max_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if max_view < all_time[i]:
                max_view = all_time[i]
                max_time = i - adv_time + 1

    start = max_time
    H = (start // 3600)
    if H < 10: H = f'0{H}'

    start = (start % 3600)
    M = (start // 60)
    if M < 10: M = f'0{M}'

    start = (start % 60)
    S = start
    if S < 10: S = f'0{S}'

    answer = f'{H}:{M}:{S}'

    return answer

play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play_time, adv_time, logs))

# 주차 요금 계산
'''
- 시간을 분으로 바꾸는 함수 필요
- 입차 출차를 기록하는 딕셔너리 필요 (key는 차량 번호로)
- fees = [기본 시간, 기본 요금, 단위 시간, 단위 요금]
    - 누적 주차 시간이 기본 시간 이하이면 기본 요금
    - 누적 추차 시간이 기본 시간을 초과하면 기본 요금 + 올림(누적 주차 시간 - 기본 시간) * 단위 시간 마다의 기본 요금
'''
import math

def change_m(time):
    h, m = time.split(':')
    m = int(h) * 60 + int(m)
    return m

def solution(fees, records):
    answer = []
    car_in_and_out_dict = {}
    for r in records:
        time, car_number, in_and_out = r.split()

        time = change_m(time)
        car_number = int(car_number)
        if car_number not in car_in_and_out_dict:
            car_in_and_out_dict[car_number] = [[]]

        if len(car_in_and_out_dict[car_number][-1]) < 2:
            car_in_and_out_dict[car_number][-1] += [time]
        else:
            car_in_and_out_dict[car_number].append([time])

    sort_car_number = sorted(list(map(int, list(car_in_and_out_dict.keys()))))
    for car_number in sort_car_number:
        total_time = 0
        for in_and_out_li in car_in_and_out_dict[car_number]:
            if len(in_and_out_li) == 2:
                in_time, out_time = in_and_out_li
                total_time += out_time - in_time
            else:
                in_time, out_time = in_and_out_li[0], change_m('23:59')
                total_time += out_time - in_time

        if total_time <= fees[0]:
            ans = fees[1]
        else:
            ans = fees[1] + (math.ceil((total_time - fees[0]) / fees[2]) * fees[3])

        answer.append(ans)

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
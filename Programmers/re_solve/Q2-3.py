from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    movig_truck = deque([])
    movig_time = deque([])
    movig_total = [movig_truck, movig_time]
    while movig_total[0] or truck_weights:
        if not truck_weights:
            if time - movig_total[1][0] >= bridge_length:
                movig_total[0].popleft()
                movig_total[1].popleft()
        else:
            if sum(movig_total[0]) + truck_weights[0] <= weight:
                movig_total[0].append(truck_weights.popleft())
                movig_total[1].append(time)

            if time - movig_total[1][0] >= bridge_length:
                movig_total[0].popleft()
                movig_total[1].popleft()
                if truck_weights:
                    if sum(movig_total[0]) + truck_weights[0] <= weight:
                        movig_total[0].append(truck_weights.popleft())
                        movig_total[1].append(time)

        time += 1

    return time
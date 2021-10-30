# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    cnt_t = len(truck_weights)
    time = 0
    moving_truck = []
    moving_time = []
    moved = []
    while len(moved) != cnt_t:
        time += 1
        if moving_truck:
            w = moving_truck[0]
            s = moving_time[0]
            if (time - s) >= bridge_length:
                moved.append([moving_truck.pop(0), moving_time.pop(0)])

        if truck_weights:
            next_t = truck_weights[0]
            if sum(moving_truck) + next_t <= weight:
                moving_truck.append(truck_weights.pop(0))
                moving_time.append(time)

    return time
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# bridge_length = 10
# weight = 10
# truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))
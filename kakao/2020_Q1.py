# 키패드 누르기
# 핵심 아이디어:
# 1. 숫자의 좌표를 먼저 구한다
# 2. y를 기준으로 손가락 위치가 결정된다!

def solution(numbers, hand):
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    numbers_xy = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    left_xy = [3, 0]
    right_xy = [3, 2]
    ret = ""
    for number in numbers:
        x, y = numbers_xy[number]
        if y == 0 :
            ret += "L"
            left_xy[0] = x
            left_xy[1] = y
        elif y == 2 :
            ret += "R"
            right_xy[0] = x
            right_xy[1] = y
        else:
            right = abs(right_xy[0] - x) + abs(right_xy[1] - y)
            left = abs(left_xy[0] - x) + abs(left_xy[1] - y)
            if right < left: # 오른쪽 손이 더 가까움
                ret += "R"
                right_xy[0] = x
                right_xy[1] = y
            elif right == left:
                if hand == "right":
                    ret += "R"
                    right_xy[0] = x
                    right_xy[1] = y
                else:
                    ret += "L"
                    left_xy[0] = x
                    left_xy[1] = y
            else:
                ret += "L"
                left_xy[0] = x
                left_xy[1] = y

    return ret

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))

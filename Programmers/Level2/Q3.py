# 멀쩡한 삼각형
def solution(w,h):
    answer = 0
    if w == h:
        answer = w * w - w
    else:
        for i in range(1, w):
            area = (h - ((h / w) * i))
            if area < 1: break
            else: answer += int(area)
        answer *= 2
    return answer
w = 8
h = 12
print(solution(w,h))

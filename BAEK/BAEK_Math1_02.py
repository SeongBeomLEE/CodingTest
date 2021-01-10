# 3KG, 5KG
# 우선 순위는 5Kg
# 1단계 주어진 Kg을 5로 나누어 떨어지는지 보단
# 2단계 5로 나누어 떨어지지 않는다면 3을 뺀 후 다시 나눠본다
# 위 과정을 계속 반복한다
# 반복하다가 Kg이 0보다 작아진다면 -1을 반환한다. (5와 3으로 안나눠 떨어진다는 소리)

def solution(kg):
    ret = 0
    while kg >= 0:
        if (kg % 5 == 0):return ret + (kg // 5)
        else:
            kg -= 3
            ret += 1
    else: return -1
kg = int(input())
print(solution(kg))

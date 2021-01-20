import sys

def mean(v):
    return round(sum(v) / len(v))

def median(v):
    v.sort()
    return v[len(v) // 2] # v의 개수는 언제나 홀수

# 중요 아이디어
# 각 값을 딕셔너리 형태로 구함
# 각 값에 밸류 값(빈도수) 중에 최대 값을 반환
# 최대 값과 동일한 key값을 리스트에 저장
# 리스트의 개수에 따라서 값을 다르게 반환
def frq(v):
    v_dict = {}
    for i in v:
        if i in v_dict:
            v_dict[i] += 1
        else:
            v_dict[i] = 1

    max_num = max(list(v_dict.values()))
    result = []
    for k in v_dict.keys():
        if v_dict[k] == max_num:
            result.append(k)
    result.sort()
    if len(result) >= 2: return result[1]
    else: return result[0]

def scope(v):
    return max(v) - min(v)

v = []
for _ in range(int(input())):
    v.append(int(sys.stdin.readline()))

print(mean(v))
print(median(v))
print(frq(v))
print(scope(v))
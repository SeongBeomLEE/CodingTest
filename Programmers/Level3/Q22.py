# 보석 쇼핑
# two_pointer
def solution(gems):
    start = 0
    end = 0
    n = len(gems)
    gems_cnt = len(set(gems))
    # 딕셔너리의 경우 O(1)에 시간 복잡도를 가짐
    gem_li = {}
    answer_li = []
    while end < n:
        if gems[end] not in gem_li:
            gem_li[gems[end]] = 1
        else:
            gem_li[gems[end]] += 1
        end += 1
        if len(gem_li) == gems_cnt:
            while start < end:
                if gem_li[gems[start]] > 1:
                    gem_li[gems[start]] -= 1
                    start += 1

                else:
                    answer_li.append([start, end])
                    break

    answer_li = sorted(answer_li, key= lambda x : (x[1] - x[0]))
    answer = answer_li[0]
    answer = [answer[0] + 1, answer[1]]
    return answer
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))
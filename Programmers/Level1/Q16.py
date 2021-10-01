# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        cnt_li = []
        cnt_li.append(i)
        for j in range(1, (i // 2) + 1):
            if i % j == 0: cnt_li.append(j)
        if len(cnt_li) % 2 == 0: answer += i
        else: answer -= i

    return answer

# 제곱수는 약수의 개수가 홀수
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

left = 13
right = 17
print(solution(left, right))
# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    for number in range(0, 10):
        if number not in numbers:
            answer += number
    return answer
numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))

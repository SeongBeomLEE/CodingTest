# 가장 큰 수
def solution(numbers):
    numbers = sorted([str(i) for i in numbers], key = lambda x: x * 3, reverse = True)
    answer = ''.join(numbers)
    return '0' if answer[0] == '0' else answer
numbers = [6, 10, 2]
print(solution(numbers))


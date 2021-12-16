def solution(numbers):
    answer = ''.join(sorted(list(map(str, numbers)), key = lambda x : x * 4, reverse = True))
    return '0' if answer[0] == '0' else answer
# 타겟 넘버
def BFS(idx, numbers, target, number, b):
    global answer
    number += b * numbers[idx]
    N = len(numbers) - 1
    if idx == N and number == target:
        answer += 1
        return
    if idx == N:
        return
    BFS(idx + 1, numbers, target, number, 1)
    BFS(idx + 1, numbers, target, number, -1)

answer = 0
def solution(numbers, target):
    global answer
    number = 0
    BFS(0, numbers, target, number, 1)
    BFS(0, numbers, target, number, -1)
    return answer

# def solution(numbers, target):
#     answer = 0
#     answer_li = [numbers[0], -numbers[0]]
#     for i in range(1, len(numbers)):
#         next_number = numbers[i]
#         _answer_li = []
#         for num in answer_li:
#             _answer_li.append(num + next_number)
#             _answer_li.append(num - next_number)
#         answer_li = _answer_li
#
#     for num in answer_li:
#         if num == target:
#             answer += 1
#     return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
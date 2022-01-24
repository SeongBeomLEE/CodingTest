# def solution(mylist):
#     answer = []
#     for i in mylist:
#         answer.append(len(i))
#     return answer
# input = [[1],[2]]
# print(solution(input))

# 아쉽네... 이렇게 풀었으면 된건데.....
from collections import deque
def solution(arr, s):
    if sum(arr) < s: return 0
    answer = 987654321
    new_arr = deque([])
    arr = deque(arr)
    while arr:
        new_arr.append(arr.popleft())
        while sum(new_arr) >= s:
            answer = min(len(new_arr), answer)
            new_arr.popleft()

    return answer

arr = [1, 2, 3, 10, 11, 12, 14, 15, 1, 1]
arr = [1, 1, 1, 1, 1]
s = 1
print(solution(arr, s))
def solution(n, m, array):
    answer = []
    for a in array:
        answer.append(min(a))
    return max(answer)

n, m = 3, 3
array = [[3, 1, 2],
         [4, 1, 4],
         [2, 2, 2]]

print(solution(n, m, array))
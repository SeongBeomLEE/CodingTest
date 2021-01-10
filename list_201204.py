def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(len(i))
    return answer
input = [[1],[2]]
print(solution(input))

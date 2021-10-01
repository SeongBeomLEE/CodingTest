# 두개 뽑아서 더하기
import itertools
def solution(numbers):
    return sorted(list(set([sum(i) for i in itertools.combinations(numbers, 2)])))
numbers = [2,1,3,4,1]
print(solution(numbers))
# 소수찾기
from itertools import permutations
def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    ret = []
    for i in range(1, len(numbers) + 1):
        ret += list(int("".join(i)) for i in map(list, permutations(list(numbers), i)))
    for i in set(ret):
        if i != 0 and i != 1:
            if is_prime(i):
                answer += 1
    return answer
numbers = '17'
# numbers = "011"
print(solution(numbers))
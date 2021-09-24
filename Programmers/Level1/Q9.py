# 소수 만들기
import itertools

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(nums):
    answer = 0
    nums = list(itertools.combinations(nums, 3))
    for num in nums:
        if is_prime_number(sum(num)): answer += 1
    return answer

nums = [1,2,3,4]
print(solution(nums))
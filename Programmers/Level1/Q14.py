# 폰켓몬
def solution(nums):
    s = len(nums) // 2
    l1 = len(set(nums))
    return l1 if l1 <= s else s

nums = [3,3,3,2,2,4]
print(solution(nums))
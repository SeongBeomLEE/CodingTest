# 스킬트리
from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        _skill = deque(list(skill))
        for st in skill_tree:
            if st in _skill:
                if _skill[0] == st:
                    _skill.popleft()
                else: break
        else:
            answer += 1

    return answer

skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
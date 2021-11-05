# 카펫
def solution(brown, yellow):
    total = brown + yellow
    for h in range(1, total):
        if total % h == 0:
            w = total // h
            if h <= w:
                if (h - 2) * (w - 2) == yellow: break
    return [w, h]
brown = 24
yellow = 24
print(solution(brown, yellow))

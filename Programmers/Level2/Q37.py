# H-index
def solution(citations):
    citations.sort(reverse = True)
    for idx, citation in enumerate(citations):
        if citation < idx + 1: break
    else: idx += 1
    return idx
citations = [41, 21]
print(solution(citations))


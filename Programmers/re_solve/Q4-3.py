def solution(citations):
    citations.sort(reverse = True)
    for no in range(1, len(citations) + 1):
        if no > citations[no - 1]:
            no = no - 1
            break
    return no
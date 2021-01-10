def solution():
    # lst 는 정렬된 리스트 [1,1,1,1]
    # lst 는 정렬된 리스트 [1,2,2,2]
    # lst 는 정렬된 리스트 [1,1,2,2]
    # lst 는 정렬된 리스트 [1,2,3,4]
    # lst 는 정렬된 리스트 [1,1,3,4]
    # lst 는 정렬된 리스트 [1,3,3,4]
    # lst 는 정렬된 리스트 [1,2,4,4]
    lst = sorted(list(map(int, input().split())))
    #같은 눈 4개
    if len(set(lst)) == 1: return 50000 + lst[0]*5000

    if len(set(lst)) == 2:
        # 같은 눈 3개
        if lst[1] == lst[2]: return 10000 + lst[1]*1000
        # 같은 눈 2개 2쌍
        return 2000 + lst[1]*500 + lst[2]*500

    # 같은 눈 2개인 것이 1개
    for i in range(3):
        if lst[i] == lst[i+1]: return 1000 + lst[i]*100

    # 모두 다 다른 눈
    return lst[3] * 100

N = int(input())
total = []
for _ in range(N):
    total.append(solution())
print(max(total))



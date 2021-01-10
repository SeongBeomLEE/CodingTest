N = int(input())
li = []
for i in range(N):
    li.append(list(map(int,input().split())))
rank_li = []
for i in range(N):
    rank = 1
    for j in range(N):
        if (li[i][0] < li[j][0]) & (li[i][1] < li[j][1]): rank +=1
    rank_li.append(rank)
print(" ".join(list(map(str,rank_li))))


# 위에서 아래로
array = []
for _ in range(int(input())):
    array.append(int(input()))
array.sort(reverse=True)
print(" ".join(list(map(str,array))))




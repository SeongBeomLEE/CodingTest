max = -1
for i in range(1,10):
    N = int(input())
    if N > max:
        max = N
        max_index = i
print(max)
print(max_index)
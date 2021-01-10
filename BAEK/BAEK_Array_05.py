N = int(input())
A = list(map(int,input().split()))
max = A[0]
for i in range(N):
    if A[i] >= max:
        max = A[i]

new_A = []
for i in A:
    new_A.append(i/max*100)

total = 0
for i in new_A:
    total = total + i

print(total/N)
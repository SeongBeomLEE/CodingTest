N = int(input())
result = 0
for i in range(1,len(str(N))):
    result += (10**i - 10**(i-1))*i
result += (N - 10**(len(str(N))-1))*len(str(N)) + len(str(N))
print(result)

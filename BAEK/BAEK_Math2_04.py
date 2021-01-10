def era(M, N):
    prime_array, prime_number = [False for _ in range(N+1)], []
    for i in range(2, N+1):
        if prime_array[i] == True: continue
        if i > M: prime_number.append(i)
        for j in range(i*i, N+1, i):
            prime_array[j] = True
    return prime_number

while True:
    M = int(input())
    if M==0: break
    print(len(era(M, 2*M)))

N, K = map(int,input().split())
coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

count = 0
coin_list.sort(reverse=True)
for coin in coin_list:
    count += K // coin
    K %= coin

print(count)
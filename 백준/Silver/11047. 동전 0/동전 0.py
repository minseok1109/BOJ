import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coin_count = 0
for coin in coins[::-1]:
    while k >= coin:
        count = k // coin
        k -= coin * (count)
        coin_count += 1 * count


print(coin_count)

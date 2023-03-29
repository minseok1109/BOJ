import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    dp[i] = numbers[i]
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + numbers[i])

print(max(dp))
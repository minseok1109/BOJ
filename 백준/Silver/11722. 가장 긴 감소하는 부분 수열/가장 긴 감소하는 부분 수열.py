import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
dp = [1] * n

temp = -sys.maxsize
for i in range(1, n):
    for j in range(0, i):
        if numbers[i] < numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

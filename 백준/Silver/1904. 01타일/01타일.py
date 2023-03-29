import sys

# 길이가 N - 2인 수열 뒤에 00을 붙이는 것과 길이가 N - 1인 수열 뒤에 1을 붙인 것의 합과 같다.
input = sys.stdin.readline
N = int(input())
dp = [0] * 1000001
dp[1], dp[2] = 1, 2
for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
print(dp[N])

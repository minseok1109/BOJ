import sys

input = sys.stdin.readline
n = int(input())
fibonacci = [None, 0, 1] + ([0] * n)

for i in range(3, n + 2):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

print(fibonacci[n + 1])

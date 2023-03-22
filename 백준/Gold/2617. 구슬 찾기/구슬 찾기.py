import sys


def dfs(arr, n):
    global count
    for i in arr[n]:
        if not visited[i]:
            visited[i] = True
            count += 1
            dfs(arr, i)


input = sys.stdin.readline
n, m = map(int, input().split())
big = [[] for _ in range(n + 1)]
small = [[] for _ in range(n + 1)]
mid = (n + 1) / 2

for _ in range(m):
    bigger, smaller = map(int, input().split())
    big[bigger].append(smaller)
    small[smaller].append(bigger)
answer = 0
for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    count = 0
    dfs(big, i)
    if count >= mid:
        answer += 1
    count = 0
    dfs(small, i)
    if count >= mid:
        answer += 1

print(answer)

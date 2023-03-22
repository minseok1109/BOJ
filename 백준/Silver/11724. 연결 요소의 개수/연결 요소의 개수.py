import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


def dfs(start):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)

import sys


def dfs(start):
    visited[start] = True
    print(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n, m, r = map(int, input().strip().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(1, n + 1):
    start, end = map(int, input().strip().split())
    graph[start].append(end)
    graph[end].append(start)
for i in graph:
    i.sort()
dfs(r)

for i in range(1, len(visited)):
    if not visited[i]:
        print(0)

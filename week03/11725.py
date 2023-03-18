import sys

sys.setrecursionlimit(10**8)


def dfs(start):
    visited[start] = 1

    for i in graph[start]:
        if not visited[i]:
            parents[i] = start
            dfs(i)


input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)
visited = [0] * (n + 1)
for _ in range(1, n):
    start, end = map(int, input().strip().split())
    graph[start].append(end)
    graph[end].append(start)


dfs(1)
for i in range(2, n + 1):
    print(parents[i])

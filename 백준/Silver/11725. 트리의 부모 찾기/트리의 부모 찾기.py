import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n = int(input())
parents = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


def dfs(start):
    for i in graph[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i)


dfs(1)
for i in range(2, n + 1):
    print(parents[i])

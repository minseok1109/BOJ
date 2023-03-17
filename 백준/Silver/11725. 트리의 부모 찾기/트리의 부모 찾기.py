import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n = int(input())
parents = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(1, n):
    start, end = map(int, input().strip().split())
    graph[start].append(end)
    graph[end].append(start)


def dfs(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)


dfs(1, graph, parents)

for i in range(2, n + 1):
    print(parents[i])

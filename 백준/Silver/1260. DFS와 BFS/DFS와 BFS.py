import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().strip().split())
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    start, end = map(int, input().strip().split())
    graph[start].append(end)
    graph[end].append(start)


def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    visited[start] = True
    queue = deque([start])
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


for i in graph:
    i.sort()
# def bfs():
visited = [False] * (n + 1)
dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)

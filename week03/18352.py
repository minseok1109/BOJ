import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n, m, k, x = map(int, input().strip().split())
cost = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    start, end = map(int, input().strip().split())
    graph[start].append(end)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                cost[i] = cost[now] + 1
                queue.append(i)


bfs(x)
if k not in cost:
    print(-1)
else:
    for i in range(1, n + 1):
        if cost[i] == k:
            print(i)

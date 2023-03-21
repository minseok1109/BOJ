import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().strip().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, input().strip().split())
    graph[start].append(end)
    indegree[end] += 1


def topologySort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(*result)


topologySort()

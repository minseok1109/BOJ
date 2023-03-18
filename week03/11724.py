import sys

input = sys.stdin.readline
N, M = map(int, input().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0


def dfs(start):
    visited[start] = True
    print(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)

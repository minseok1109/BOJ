import sys

input = sys.stdin.readline
n = int(input())
e = int(input())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0


def dfs(start):
    global count
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            count += 1
            dfs(i)


dfs(1)
print(count)

import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().strip().split())

visited = [False] * (n + 1)
graph = [list(map(int, input().strip().split())) for _ in range(m)]


# 재귀 or stack
def dfs(start):
    visited = []
    stack = []
    for node in graph:
        if node[0] == start:
            stack.append(node[1])
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            for node in graph:
                if node[0] == now and node[1] not in visited:
                    stack.append(node[1])
            print(now, end=" ")
        else:
            continue


# 큐
def bfs(start):
    visited = []
    queue = deque([start])
    for node in graph:
        if node[0] == start:
            queue.append(node[1])
    while queue:
        now = queue.popleft()
        if now not in visited:
            visited.append(now)
            for node in graph:
                if node[0] == now and node[1] not in visited:
                    queue.append(node[1])
            print(now, end=" ")
        else:
            continue


# bfs(1)
dfs(1)


def dfs_stack(start):
    stack = [start]
    visited[start] = True
    print(start, end=" ")

    while stack:
        cur = stack[-1]
        found = False

        for i in graph[cur]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                print(i, end=" ")
                found = True
                break

        if not found:
            stack.pop()

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

edges = {}

for i in range(1,N+1):
    edges[i] = []

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

def bfs(start):
    visited = [False] * (N+1)
    kevin = [0] * (N+1)
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for w in edges[v]:
            if not visited[w]:
                visited[w] = True
                kevin[w] = kevin[v] + 1
                queue.append(w)
    return sum(kevin)

result = []
for i in range(1,N+1):
    result.append(bfs(i))

print(result.index(min(result))+1)
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)


def dfs(outdoor: int):
    indoor = 0
    for i in graph[outdoor]:
        if roads[i - 1] == 0:
            if i not in visited:
                visited.add(i)
                indoor += dfs(i)
        else:
            indoor += 1
    return indoor


input = sys.stdin.readline
n = int(input())  # 정점의 개수
roads = list(map(int, list(input().strip())))
graph = defaultdict(list)
all_counts = 0

for _ in range(n - 1):
    start, end = map(int, input().strip().split())
    graph[start].append(end)
    graph[end].append(start)
    if roads[start - 1] == 1 and roads[end - 1] == 1:
        all_counts += 2

visited = set()
for i in range(1, n + 1):
    indoor = 0
    if roads[i - 1] == 0:
        if i not in visited:
            visited.add(i)
            indoor = dfs(i)
    all_counts += indoor * (indoor - 1)

print(all_counts)

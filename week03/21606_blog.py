import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)


def DFS(outdoor: int):
    indoor = 0
    for i in net[outdoor]:
        if roads[i - 1] == 0:
            if i not in visited:
                visited.add(i)
                indoor += DFS(i)
        else:
            indoor += 1

    return indoor


N = int(input())
roads = list(map(int, list(input())))  # 장소 n에 대하여 A[n-1]이 1이면 실내, 0이면 실외.
net = defaultdict(list)
route_count = 0

for _ in range(N - 1):
    start, end = map(int, sys.stdin.readline().split())
    net[start].append(end)
    net[end].append(start)
    if roads[start - 1] == 1 and roads[end - 1] == 1:
        route_count += 2  # 실내끼리 인접했을 경우 경로를 2개 더해준다.

visited = set()
for i in range(1, N + 1):
    indoor = 0
    if roads[i - 1] == 0:
        if i not in visited:
            visited.add(i)
            indoor = DFS(i)

    route_count += indoor * (indoor - 1)

print(route_count)

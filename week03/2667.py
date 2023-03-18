import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n = int(input())
city = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
dxdy = list(zip(dx, dy))


def isValid(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y, visited, dfs_count):
    if isValid(x, y):
        if city[x][y] == 1 and (x, y) not in visited:
            for dx, dy in dxdy:
                tmp_x, tmp_y = x + dx, y + dy
                # 2차원 배열을 안넘어가면서 다음 도시가 1이고 아직 방문하지 않았다면
                x, y = tmp_x, tmp_y
                visited.add((x, y))
                dfs_count += 1
                visited, dfs_count = dfs(x, y, visited, dfs_count)
            return visited, dfs_count


results = []
visited = set()
for x in range(n):
    for y in range(n):
        if city[x][y] == 1 and (x, y) not in visited:
            dfs_count = 1
            visited.add((x, y))
            visited, dfs_count = dfs(x, y, visited, dfs_count)
            results.append(dfs_count)

print(len(results))
for i in sorted(results):
    print(str(i))

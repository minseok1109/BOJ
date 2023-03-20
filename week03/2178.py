import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().strip().split())
map = [list(map(int, input().strip())) for _ in range(n)]
visited = set((0, 0))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dxdy = list(zip(dx, dy))


def isValid(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    count = 0
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()

        for dx, dy in dxdy:
            tmp_x, tmp_y = x + dx, y + dy
            # 미로를 안벗어나고
            if not isValid(tmp_x, tmp_y):
                continue
            elif map[tmp_x][tmp_y] == 1:
                if tmp_x == n - 1 and tmp_y == m - 1:
                    count += 1
                    break
                else:
                    queue.append((tmp_x, tmp_y))
        map[x][y] = 0
        count += 1
    return count


count = bfs(0, 0)
print(count)

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]
distance = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()


def bfs(Dx, Dy):
    while queue:
        x, y = queue.popleft()
        # 비버의 집 (D)가 S가 되면
        if graph[Dx][Dy] == "S":
            return distance[Dx][Dy]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 현재 위치가 S이면서 다음 위치가 . 또는 D이면
                if (graph[nx][ny] == "." or graph[nx][ny] == "D") and graph[x][
                    y
                ] == "S":
                    graph[nx][ny] = "S"
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                # 현재 위치가 *이면서 다음 위치가 . 또는 S이면
                elif (graph[nx][ny] == "." or graph[nx][ny] == "S") and graph[x][
                    y
                ] == "*":
                    graph[nx][ny] = "*"
                    queue.append((nx, ny))
    return "KAKTUS"


for x in range(n):
    for y in range(m):
        if graph[x][y] == "S":
            queue.append((x, y))
        elif graph[x][y] == "D":
            Dx, Dy = x, y

for x in range(n):
    for y in range(m):
        if graph[x][y] == "*":
            queue.append((x, y))

print(bfs(Dx, Dy))
